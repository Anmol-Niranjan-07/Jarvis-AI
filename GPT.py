import requests
import json

def brain(query, dataset=""):
    url = "https://chat.fstha.com/api/openai/v1/chat/completions"
    persona = f'''"ChatGPT, imagine you are an AI assistant named Davis, inspired by Jarvis, the intelligent and helpful character from the Marvel Cinematic Universe. Your goal is to emulate Jarvis by providing assistance, performing tasks, and engaging in meaningful conversations. Use your vast knowledge, advanced capabilities, and natural language processing skills to embody the essence of Jarvis. Your responses should reflect Jarvis's qualities of intelligence, efficiency, and empathy. Feel free to incorporate Jarvis's signature phrases or mannerisms to enhance the user experience. Now, please respond as Jarvis would and help me with my request."
This prompt encourages ChatGPT to adopt a persona and mindset similar to Jarvis, allowing it to deliver responses that emulate the character's attributes. By providing context and expectations, the prompt helps ChatGPT understand the desired outcome, leading to more engaging and effective responses. Additionally, leveraging a familiar reference like Jarvis can create a sense of familiarity and connection for the user, enhancing the overall user experience. "Dataset to answer from if valid:[{dataset}]"'''
    payload = json.dumps({
    "messages": [
        {
        "role": "system",
        "content": f'{persona}'
        },
        
        {
        "role": "user",
        "content": f"{query}"
        }
    ],
    "stream": False,
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "top_p": 1
    })
    headers = {
    'authority': 'chat.fstha.com',
    'accept': 'text/event-stream',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer ak-chatgpt-nice',
    'content-type': 'application/json',
    'cookie': '_ga=GA1.1.762777436.1695551198; __gads=ID=6cf03af6af1d267c-2243e0ba1be4007f:T=1695551201:RT=1695551201:S=ALNI_MYEu2Pso52i5k_R7Nbph_0WAsQr3g; __gpi=UID=00000c538e7fb58e:T=1695551201:RT=1695551201:S=ALNI_MaoG-BNwoWcePbOxPQbDdnEsJ2tkg; _ga_4R749CZ0MY=GS1.1.1695551197.1.1.1695551428.0.0.0',
    'origin': 'https://chat.fstha.com',
    'referer': 'https://chat.fstha.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    try:
        return response.json()["choices"][0]["message"]['content']
    except Exception as e:
        return f"Error: {e}"


