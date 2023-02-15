import openai
from decouple import config

openai.api_key = config('api_key')

while True:

    prompt = input("\n Introduce una pregunta: ")

    if prompt == "exit":
        break

    complection = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000
    )

    print(complection.choices[0].text)