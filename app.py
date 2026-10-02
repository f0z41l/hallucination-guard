import ollama

question = input("Enter your question: ")

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

answer = response["message"]["content"]

print("\nGenerated Answer:")
print(answer)