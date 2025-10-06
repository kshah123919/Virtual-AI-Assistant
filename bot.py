import openai

client = openai.OpenAI(api_key="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")  # Use your actual key

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! 👋")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)









