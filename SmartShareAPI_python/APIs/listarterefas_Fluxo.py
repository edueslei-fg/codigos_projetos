import requests, logging, json, os      #|
from dotenv import load_dotenv          #| Importação de Bibliotecas.
import json

load_dotenv();      #| Faz a Chamada do .env para extrair as informações.

TOKEN = os.getenv("token")
API_BASE = os.getenv("API_BASE")            #|
API_CLIENT = os.getenv("API_CLIENT")        #|
USUARIO = os.getenv("USUARIO")              #| Extrai as informações do .env.
SENHA = os.getenv("SENHA")                  #|
AUTENTICACAO = os.getenv("AUTENTICACAO")    #|
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")    #|

#cod_Processo = input("Qual o código do processo? : ")       #| Código do Fluxo que será pulado.
#cod_Fluxo = input("Qual o código do Fluxo? : ")

def ListarTarefas_Fluxo():      #| Faz o chamado da API para Avanço de Fluxo Forçado.
    url = f"{API_BASE}/api/v1/Tarefa/DetalharTarefa"      #| Faz a conexão com a API do Smart Share.
    headers = {
        "Accept": "application/json",
        "dsCliente": "mobile",
        "dsChaveAutenticacao": str(AUTENTICACAO),
        "tokenUsuario": str(TOKEN),
        "cdProcesso": "27",
        "cdFluxo": "3319"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    json_data = response.json()
    tarefas = json_data.get("lstTarefas", [])
    print("Qtd tarefas:", len(tarefas))

    for t in tarefas:
        print(
        "Tarefa:", t["cdTarefa"],
        "| Status:", t["dsStatus"],
        "| Fluxo:", t["cdFluxo"]
        )
    print(response.status_code)
    print(response.text)

    return tarefas

print(ListarTarefas_Fluxo()) #| Chama a Função para Executar o Processo