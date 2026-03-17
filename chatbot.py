from openai import OpenAI

# create client with groq api
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

print("Simple AI Chatbot")
print("Type 'exit' to stop")

while True:

    # take user input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # send request to llm
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    # extract reply
    answer = response.choices[0].message.content

    # print response
    print("Bot:", answer)
