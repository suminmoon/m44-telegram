from flask import Flask, request
import requests
from decouple import config

app = Flask(__name__)
token = config('TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

# http://127.0.0.1/
@app.route('/')
def root():
    return 'happy hacking'


# import pprint -> formatting 형태로 뽑아내기
@app.route(f'/{token}', methods=['POST'])
def telegram():
    message = request.get_json().get('message')
    if message is not None:
        chat_id = message.get('from').get('id')
        text = messate.get('text')
        requests.get(f'{api_url}/sendMessage?chat_id = {chat_id}&text = {text}')

    return '', 200





if __name__ == '__main__':
    app.run(debug=True)
