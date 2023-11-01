import openai

openai_api_key = "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"
# passa os dados da api pra Openai pra poder consumir os dados da api

openai.api_key = openai_api_key

def send_message(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo"
        messages = [
            {"role": "user", "content": mensagem}
        ]
    )

    return response["choices"][0]
# retorna a resposta que esta dentro do dicionario resposta que contem a key "choices" ~com a resposta