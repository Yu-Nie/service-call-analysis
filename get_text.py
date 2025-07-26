# Install the assemblyai package by executing the command "pip install assemblyai"

import assemblyai as aai

aai.settings.api_key = "***"

audio_file = "/Downloads/Takehome/audio.m4a"
# audio_file = "https://assembly.ai/wildfires.mp3"

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

with open("transcript.txt", "w") as fp:
  fp.write(transcript.text)
# print(transcript.text)
