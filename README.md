# Dockerized Email Generator - Deep Email

The Deep Email project helps users generate emails with subject lines based on prompts. The Chainlit package is used to build a chat UI through which users can communicate with the LLM to get their desired email generated.

### Usage Instructions:

1. **Dependencies:**
   - Docker

2. **Clone the repository:**
   ```bash
   git clone https://github.com/AbbiJay/deepemail.git
   cd DeepEmail
   ```

3. **Create Docker Image:**
   ```bash
   docker build -t img_deepemail:latest .
   ```

4. **Create and Run Docker Container:**
   ```bash
   docker run --name con_deepemail -p 8000:8000 -v /path/to/DeepEmail:/app img_deepemail:latest
   ```

5. **Access the Chainlit Chat UI:**
   - Visit [http://localhost:8005/](http://localhost:8005/) to access the Chainlit chat UI.

### Fine-Tuning Instructions:

- To fine-tune Falcon 7B on your own dataset, use the `EmailFineTuned_Falcon_7B.ipynb` notebook available in this repository. You can download the fine-tuned model from [Hugging Face](https://huggingface.co/AJ02/Updated-FineTuned-Falcon-7b).

---

Make sure to replace `/path/to/DeepEmail` with the actual path on your Docker host where the repository is located. 
