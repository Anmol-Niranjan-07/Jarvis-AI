import base64
import io
from pydub import AudioSegment
import random
import subprocess
import requests
def speak(text):
    url = "https://audio.api.speechify.dev/generateAudioFiles"

    payload = '{"audioFormat":"mp3","paragraphChunks":[$~],"voiceParams":{"name":"Snoop","engine":"resemble","languageCode":"en-US"}}'.replace("$~", f'"{text}"')
    headers = {
    'authority': 'audio.api.speechify.dev',
    'accept': '*/*',
    'accept-base64': 'true',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://soundbite.speechify.com',
    'referer': 'https://soundbite.speechify.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
    'x-speechify-client': 'API',
    'x-speechify-client-version': '0.1.295'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # Replace this with your base64-encoded audio string
    base64_audio = response.json()['audioStream']

    audio_data = base64.b64decode(base64_audio)

    audio = AudioSegment.from_file(io.BytesIO(audio_data))

    temp_wav_file = f"./spoken_audios/temp_audio_{random.randint(1,1000000000)}.wav"
    audio.export(temp_wav_file, format="wav")
    print(text)
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-loglevel", "error", "-hide_banner", temp_wav_file], shell=True)
    