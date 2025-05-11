import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
import sys
from pydub import AudioSegment
from config import VIDEOS_PATH, MP3_AUDIOS_PATH, WAV_AUDIOS_PATH, TRANSCRIPTIONS_PATH
import os
import whisper

FILE_NAME = sys.argv[1]

# Convert to MP3
path = f"{VIDEOS_PATH}/{FILE_NAME}.mp4"
clip = mp.VideoFileClip(path).subclip()

if not os.path.isdir(f'{MP3_AUDIOS_PATH}/{FILE_NAME}'):
    os.mkdir(f'{MP3_AUDIOS_PATH}/{FILE_NAME}')

clip.audio.write_audiofile(f"{MP3_AUDIOS_PATH}/{FILE_NAME}/{FILE_NAME}.mp3")

src=(f"{MP3_AUDIOS_PATH}/{FILE_NAME}/{FILE_NAME}.mp3")
sound = AudioSegment.from_mp3(src)

if not os.path.isdir(f'{WAV_AUDIOS_PATH}/{FILE_NAME}'):
    os.mkdir(f'{WAV_AUDIOS_PATH}/{FILE_NAME}')

sound.export(f"{WAV_AUDIOS_PATH}/{FILE_NAME}/{FILE_NAME}.wav", format="wav")
file_audio = sr.AudioFile(f"{WAV_AUDIOS_PATH}/{FILE_NAME}/{FILE_NAME}.wav")

# Extract text from audio

model = whisper.load_model("large")
audio_path = f"{MP3_AUDIOS_PATH}/{FILE_NAME}/{FILE_NAME}.mp3"
print("Transcrevendo o áudio... Isso pode levar um tempo.")

result = model.transcribe(audio_path)

if not os.path.isdir(f'{TRANSCRIPTIONS_PATH}/{FILE_NAME}'):
    os.mkdir(f'{TRANSCRIPTIONS_PATH}/{FILE_NAME}')

txt_path = f"{TRANSCRIPTIONS_PATH}/{FILE_NAME}/transcricao{FILE_NAME}.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcrição salva em {txt_path}")