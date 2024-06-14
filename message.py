# pip install openai==0.28

import openai
import chatGPT # arquivo com a api key poderia ser uma env também

openai.api_key = chatGPT.api_key

# Define the model engine
model_engine = "gpt-3.5-turbo"

# Get user input
teste = input("Faça sua pergunta: ")

# Create a completion using the new API method
response = openai.ChatCompletion.create(
    model=model_engine,
    messages=[
        {"role": "system", "content": "Você é um assistente de IA."}, #  passar para o chat gpt o que você quer que ele faça
        # {"role": "assistant", "content": "O que o chat GPT ira responder"},
        {"role": "user", "content": teste} #  o que o usuário está perguntando
    ],
    max_tokens=1024,
    temperature=0.7
)

# Print the response
if response is not None and response.choices is not None:
    print("A resposta encontrada foi:")
    for choice in response.choices:
        print(choice.message["content"])
