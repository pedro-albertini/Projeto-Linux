import requests
from datetime import datetime
import subprocess

URL = "SEU_IP"
TOKEN = "SEU_TOKEN"
CHAT_ID = "SEU_CHAT"
MENSAGEM = "ALERTA!! Site fora do ar!"

def mensagem_telegram(mensagem):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": mensagem}
        resposta = requests.post(url, data=data)
        return resposta.json()
        
def reiniciar_nginx():
        subprocess.run(["sudo","systemctl","restart","nginx"],check=True)
        print(f"{datetime.now()} - Servidor reiniciado com sucesso")
        
def monitoramento():
        try:
                resposta = requests.get(URL, timeout=10)
                if resposta.status_code == 200:
                        print(f"{datetime.now()} - Site está online")
                else:
                        mensagem_telegram(MENSAGEM)
                        print(f"{datetime.now()} - Site está fora do ar")
                        reiniciar_nginx()
        except requests.RequestException:
                mensagem_telegram(MENSAGEM)
                print(f"{datetime.now()} - Site está fora do ar")
                reiniciar_nginx()
                
if __name__ == "__main__":
        monitoramento()
