import openai

openai.api_key = "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"
def generate_response(prompt):
    response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            temperature = 0.7,
            max_tokens = 500,
            n = 1,
            stop = None,
            )
    return response.choices[0].text.strip()

while True:
    user_input = input('User: ')
    prompt = f"user: {user_input}\nChatGPT: "
    response = generate_response(prompt)
    print("ChatGPT: ",response)
