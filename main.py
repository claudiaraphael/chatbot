import openai
# retorna a resposta que esta dentro do dicionario resposta que contem a key "choices" ~com a resposta dentro de uma lista (ta na documentação)
# https://platform.openai.com/docs/guides/gpt/chat-completions-api


openai_key = "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"
# passa os dados da api pra Openai pra poder consumir os dados da api

openai.api_key = openai_key

def send_message(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": message}
        ]
    )

    return response["choices"][0]["message"]

print(send_message("What's the medium price for coffee in Brazil?"))

# excedeu a quota do chatgpt entao como nao tenho premium vou continuar depois pra poder continuar testando enquanto desenvolvo
# link do tutorial: https://www.youtube.com/watch?v=vGn4yAsIpkU&t=25s
