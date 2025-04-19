from openai import OpenAI

client = OpenAI(
    api_key="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"
)

# Check available models
try:
    models = client.models.list()
    print("Available models:", [model.id for model in models.data])
except Exception as e:
    print("Error listing models:", e)

# Try to create completion
try:
    completion = client.chat.completions.create(
        model="gpt-4.1-2025-04-14",
        messages=[
            {"role": "system", "content": "You are a virtual assistant"},
            {"role": "user", "content": "what is coding?"}
        ]
    )
    print(completion.choices[0].message)
except Exception as e:
    print("Error during completion:", e)