import requests
from datetime import datetime

URL = "http://172.22.64.106"
TOKEN = "7573522611:AAFwDQCxhd2VD1uF6nop_xiYT6g6thrvBKg"
CHAT_ID = "6801410508"
MENSAGEM = "ALERTA!! Site fora do ar!"

def mensagem_telegram(mensagem):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": mensagem}
        resposta = requests.post(url, data=data)
        return resposta.json()

def monitoramento():
        try:
                resposta = requests.get(URL, timeout=10)
                if resposta.status_code == 200:
                        print(f"{datetime.now()} - Site está online")
        except requests.RequestException:
                mensagem_telegram(MENSAGEM)
                print(f"{datetime.now()} - Site está fora do ar")

if __name__ == "__main__":
        monitoramento()
