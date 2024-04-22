FROM python
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

VOLUME /app

ENV HUGGINGFACEHUB_API_TOKEN=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

CMD ["chainlit", "run", "langchain_falcon.py", "--no-cache", "-w"]
