
# Sistema de Monitoramento do Servidor [Linux]

Esse projeto faz parte do programa de bolsas da Compass UOL na trilha de DevSecOps.

Ele envolve a criação e configuração de um servidor localmente, automação de monitoramento e notificações via telegram. Sempre que ouver quedas ou desligamento do servidor web, o script enviará automaticamente uma notificação a cada minuto alertando sobre o problema via telegram.
## Indice

 - [Instalando o NGINX](#instalando-o-NGINX)
 - [Ativação NGINX](https://github.com/matiassingers/awesome-rea)
 - [Configuração SystemD](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Pagina WEB](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Ativação NGINX](https://github.com/matiassingers/awesome-rea)
 - [Configuração SystemD](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Instalando o NGINX

Antes de instalar atualize a lista de pacotes disponiveis e suas versões:

```bash
  sudo apt-get update
```

Agora instale o NGINX:

```bash
  sudo apt-get install nginx
```

## Configuração SystemD

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



## Uso/Exemplos

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  npm run test
```

