import requests, logging, json, os      #|
from dotenv import load_dotenv          #| Importação de Bibliotecas.
from json import json_data;z

load_dotenv();      #| Faz a Chamada do .env para extrair as informações.

API_BASE = os.getenv("API_BASE")            #|
API_CLIENT = os.getenv("API_CLIENT")        #|
USUARIO = os.getenv("USUARIO")              #| Extrai as informações do .env.
SENHA = os.getenv("SENHA")                  #|
AUTENTICACAO = os.getenv("AUTENTICACAO")    #|
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")    #|

cod_Processo = input("Qual o código do processo? : ")       #| Código do Fluxo que será pulado.
cod_Fluxo = input("Eual o código do Fluxo")



token = "914AD8F80F261CF25CF285E9E29C9DDDFDBA5E69"        #| Faz o Chamado da Função para gerar o token.

def ListarTarefas_Fluxo():      #| Faz o chamado da API para Avanço de Fluxo Forçado.
    url = f"{API_BASE}/api/v1/Tarefa/ListarTarefasPorUsuario"      #| Faz a conexão com a API do Smart Share.
    headers = {         #| Define as variaveis do Header.
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdProcesso": cod_Processo, 
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),    #| Token gerado pelo Smart Share. 
    }
    print("FLUXO:", cod_Processo) 

    body = {         #| Informações queserão enviadas ao Servidor.
        "cdFluxo":  cod_Fluxo,
        "dsFluxo": str(),


    }
    tarefas = dados["lstTarefas"]

    print(tarefas)
    response = requests.get(url, headers=headers, json=body)
    tarefas =  json_data.get();       #| Dá resposta do processo da API 
    print("STATUS:", response.status_code)      #|
    print("BODY:", response.text)               #| Retorna a resposta do processo feito no Smart Share
    print(response.request.headers)             #| 
    print(response.request.body)                #| 

    response.raise_for_status()
    return response

print(ListarTarefas_Fluxo()) #| Chama a Função para Executar o Processo