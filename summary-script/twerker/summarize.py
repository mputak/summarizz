import openai, config, transcribe

print("Original: ", transcribe.transcript)

openai.api_key = config.API_KEY
response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt= f"You will summarize the following text: {transcribe.transcript['text']}."
)

# print("Summarized: ", response['choices'][0]['text'])
