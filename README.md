
# Sistema de Monitoramento do Servidor [Linux]

Esse projeto faz parte do programa de bolsas da Compass UOL na trilha de DevSecOps.

Ele envolve a criação e configuração de um servidor localmente, automação de monitoramento e notificações via telegram. Sempre que ouver quedas ou desligamento do servidor web, o script enviará automaticamente uma notificação a cada minuto alertando sobre o problema via telegram.
## Indice

 - [Instalando o NGINX](#Instalando-o-NGINX)
 - [Ativando o NGINX](#Ativando-o-NGINX)
 - [Configurando o SystemD](#Configurando-o-SystemD)
 - [Página Web](Página-Web)
 - [Criando o Bot do Telegram](#Criando-o-Bot-do-Telegram)
 - [Criando o Script de Monitoramento](#Criando-o-Script-de-Monitoramento)
 - [Automatizando o Script e Registros(logs)](#Automatizando-o-Script-e-Registros(logs))


## Instalando o NGINX

Antes de instalar atualize a lista de pacotes disponiveis e suas versões:

```bash
  sudo apt-get update
```

Agora instale o NGINX:

```bash
  sudo apt-get install nginx
```
## Ativando o NGINX

Apos a instalação, o primeiro passo é iniciar o serviço NGINX:

```bash
  sudo systemctl start nginx
```

Agora habilite ele para iniciar junto com a inicialização do sistema:

```bash
  sudo systemctl enable nginx
```

## Configurando o SystemD

Para que o nginx reinicialize automaticamente caso haja queda, precisamos editar o arquivo de serviço dele:

```bash
  sudo nano /usr/lib/systemd/system/nginx.service 
```

Na edição em [Service] adicione essas duas linhas:

```bash
  Restart=always 
  RestartSec=5s 
```

Agora recarrege os arquivo de serviço (.service) do systemd:

```bash
  sudo systemctl daemon-reload
```

Reinicie o nginx:

```bash
  sudo systemctl restart nginx
```

Para teste se está reinciando automaticamente:

```bash
  sudo systemctl status nginx
  sudo pkill -9 nginx
  sudo systemctl status nginx
```

## Página Web

## Criando o Bot do Telegram

Na barra de busca do Telegram execute '@BotFather' e crie um bot a partir dele:

  - /start: começa a criação do bot
  - /newbot: precisará colocar algumas informações do bot
  - Recebido o TOKEN seu bot estará criado

Para obter o Id do chat do seu bot, acesse o endereço a seguir alterando o seu TOKEN:

```bash
  https://api.telegram.org/bot<TOKEN>/getUpdates
```

## Criando o Script de Monitoramento

Navegue até o diretório que script irá ficar:

```bash
  cd /usuario
```

Crie o script e coloque o conteúdo nele:

```bash
  sudo nano script.py
```

Agora de permissão pro script ser executado:

```bash
  chmod +x script.py
```

## Automatizando o Script e Registros(logs)

Edite a lista de tarefas:

```bash
  sudo crontab -e
```

Adicione a tarefa a ser realizada e guarde o registro no arquivo.log do script no caminho que desejar, no caso dos arquivos .py o caminho aonde o python está na sua máquina também precisa estar no comando:

```bash
  ***** /usr/bin/python3 /usuario/script.py >> /var/log/script.log
```

Verifique se o agendamento foi feito corretamente

```bash
  sudo crontab -l
```
