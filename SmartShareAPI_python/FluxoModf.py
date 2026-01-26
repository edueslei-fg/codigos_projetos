import requests, logging, json, os      #|
from dotenv import load_dotenv          #| Importação de Bibliotecas.
import json                             #|

load_dotenv();      #| Faz a Chamada do .env para extrair as informações.

API_BASE = os.getenv("API_BASE")            #|
API_CLIENT = os.getenv("API_CLIENT")        #|
USUARIO = os.getenv("USUARIO")              #| Extrai as informações do .env.
SENHA = os.getenv("SENHA")                  #|
AUTENTICACAO = os.getenv("AUTENTICACAO")    #|
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")    #|

cod_fluxo = input("Qual o código do processo? : ")       #| Código do Fluxo que será pulado.
Email = input("Email ADM Cadastrado:");            #| Email do Administrador que avançará o Fluxo.

def call_api_login():           #| Função para gerar token e validação do Usuário.
    url = f"{API_BASE}/api/v2/Usuario/ValidarLogin"     #| Faz conexção com a API do Smart Share.
    files = {
        'dsUsuario': (None, 'root.fg'), #|Login Root FG.
        'dsSenha': (None, 'Fg@2025@')   #|
    }
    headers = {'dsCliente': API_CLIENT, 'dsChaveAutenticacao': AUTENTICACAO}     #| Chama a autenticação de Login no Share Com o POST Header.
    resp = requests.post(url, headers=headers, files=files)     #| Dá a reposta do servidor .
    resp.raise_for_status()         #| Levanta a resposta ao processo.
    token = resp.json().get("tokenUsuario")     #| Dá um chamado de resposta para extrair o Token para o acesso com login root.fg.
    logging.info("Login OK, token recebido")
    return token    #Retorna Token para uso abaixo.

token = call_api_login()        #| Faz o Chamado da Função para gerar o token.

def pular_fluxo():      #| Faz o chamado da API para Avanço de Fluxo Forçado.
    url = f"{API_BASE}/SmartshareAPI/api/v1/Fluxo/AvancaFluxo"      #| Faz a conexão com a API do Smart Share.
    headers = {         #| Define as variaveis do Header.
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdFluxo": str(cod_fluxo), 
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),         #| Token gerado pelo Smart Share.
        "dsEmailExecutor": str(Email) 
    }
    print("FLUXO:", cod_fluxo) 

    body = {         #| Informações queserão enviadas ao Servidor.
      "cdFluxo":  str(cod_fluxo),  
      "dsEmailExecutor": f"{Email}"     #| Email do ADM que será responsavel pela 
    }
    response = requests.post(url, headers=headers, json=body)       #| Dá resposta do processo da API 
    print("STATUS:", response.status_code)      #|
    print("BODY:", response.text)               #| Retorna a resposta do processo feito no Smart Share
    print(response.request.headers)             #| 
    print(response.request.body)                #| 

    response.raise_for_status()
    return response

print(pular_fluxo()); #| Chama a Função para Executar o Processo