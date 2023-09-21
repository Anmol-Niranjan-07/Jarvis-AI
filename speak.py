import base64  # Importing the base64 library for encoding/decoding operations
import io  # Importing the io library for handling stream operations
from pydub import AudioSegment  # Importing AudioSegment from pydub for audio processing
import random  # Importing the random library for generating random numbers
import subprocess  # Importing the subprocess library for running new applications/processes
import requests  # Importing the requests library for making HTTP requests
import os  # Importing the os library for handling OS operations
def speak(text):  # Defining the speak function that takes text as input
    url = "https://audio.api.speechify.dev/generateAudioFiles"  # URL of the API that generates audio files

    # Preparing the payload for the POST request. The text to be converted to speech is inserted into the payload.
    payload = '{"audioFormat":"mp3","paragraphChunks":[$~],"voiceParams":{"name":"Snoop","engine":"resemble","languageCode":"en-US"}}'.replace("$~", f'"{text}"')
    # Setting up the headers for the POST request
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

    # Making the POST request to the API and storing the response
    response = requests.request("POST", url, headers=headers, data=payload)

    # Extracting the base64-encoded audio string from the response
    base64_audio = response.json()['audioStream']

    # Decoding the base64 audio string to get the audio data
    audio_data = base64.b64decode(base64_audio)

    # Creating an AudioSegment object from the audio data
    audio = AudioSegment.from_file(io.BytesIO(audio_data))
    # Check if the 'spoken_audios' directory exists, if not, create it
    if not os.path.exists('spoken_audios'):
        os.makedirs('spoken_audios')
    
    # Creating a temporary wav file to store the audio
    temp_wav_file = f"./spoken_audios/temp_audio_{random.randint(1,1000000000)}.wav"
    # Exporting the audio to the wav file
    audio.export(temp_wav_file, format="wav")
    # Printing the text
    print(text)
    # Playing the audio file using ffplay
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-loglevel", "error", "-hide_banner", temp_wav_file], shell=True)
