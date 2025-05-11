import os
from dotenv import load_dotenv

load_dotenv()

FILE_NAME = os.getenv('FILE_NAME')
VIDEOS_PATH = os.getenv('VIDEOS_PATH')
MP3_AUDIOS_PATH = os.getenv('MP3_AUDIOS_PATH')
WAV_AUDIOS_PATH = os.getenv('WAV_AUDIOS_PATH')
TRANSCRIPTIONS_PATH = os.getenv('TRANSCRIPTIONS_PATH')