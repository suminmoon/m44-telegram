import requests
from decouple import config

def send_message(text):
    token = config('TOKEN')
    api_url = f'https://api.telegram.org/bot{token}'

    response = requests.get(api_url + '/getUpdates').json()
    chat_id = response['result'][0]['message']['from']['id']

    requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

