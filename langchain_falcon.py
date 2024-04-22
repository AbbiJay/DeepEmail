from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Run command - 
# chainlit run langchain_falcon.py --no-cache -w

# from dotenv import load_dotenv
import chainlit as cl

# Load environment variables from .env file
# load_dotenv()


HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACE_API_TOKEN")

repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceEndpoint(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN, 
                     repo_id=repo_id, temperature=0.5, max_new_tokens=300)

#Your answer: 
template = """
You are a helpful AI E-mail assistant who helps write e-mails. I give you a prompt and you must give me the subject text for the email and the email text for the prompt.
Please provide a well-written email, including a subject line and body, in response to the following prompt:
{question}
Please ensure that the email is professional, informative, and engaging. The subject line should be clear and concise, and the body of the email should be well-organized and easy to read.
"""

conversation_history = []

@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    # Reset the conversation history when a new chat starts
    global conversation_history
    conversation_history = []

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def main(message: str):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Check if the message is a command to clear the chat history
    if message.content.lower() == "clear chat":
        global conversation_history
        conversation_history = []
        await cl.Message(content="Chat history cleared.").send()
        return

    # Append the current message to the conversation history
    conversation_history.append(message)

    # Generate response based on the entire conversation history
    input_text = "\n".join(msg.content for msg in conversation_history)
    res = await llm_chain.acall(input_text, callbacks=[cl.AsyncLangchainCallbackHandler()])

    # Send the response
    await cl.Message(content=res["text"]).send()