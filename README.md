# Dockerized Email Generator - Deep Email
The current project helps users generate emails with subject line based on prompts. The chainlit package is used to build a chat UI using which users can communicate with the LLM to get their desired email generated.
Below are the steps to follow to run the Deep Email project

## 1. Dependencies
  - Docker
    
## 2. Clone the repository

## 3. Create Docker Image
` docker build -t img_deepemail:latest . `

## 4. Create and Run Docker Continer
` docker run --name con_deepemail -p 8000:8000 -v C:\Users\hp\Documents\GitHub\DockerizedEmailGenerator:\app img_deepemail:latest `

## 5. Follow http://localhost:8005/ to access the chainlit chat UI

