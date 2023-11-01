import openai
# retorna a resposta que esta dentro do dicionario resposta que contem a key "choices" ~com a resposta dentro de uma lista (ta na documentação)
# https://platform.openai.com/docs/guides/gpt/chat-completions-api


openai_api_key = "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"
# passa os dados da api pra Openai pra poder consumir os dados da api

openai.api_key = openai_api_key

def send_message(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": message}
        ]
    )

    return response["choices"][0]["message"]

print(send_message("What's the medium price for weed in Toronto?"))