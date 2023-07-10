import openai, config

file_location = "twerker/recorded.wav"

openai.api_key = config.API_KEY
audio_file = open(file_location, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
