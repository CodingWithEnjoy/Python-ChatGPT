import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

model_engine = "text-davinci-003"

prompt = input("Enter New Prompt : ")

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
)

response = completion.choices[0].text
print(response)
