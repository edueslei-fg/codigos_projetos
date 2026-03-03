import requests, logging, json, os
from dotenv import load_dotenv
import json
from load_dependencias import API_BASE, API_CLIENT, AUTENTICACAO
from API_Login import call_api_login

def Ver_Tarefa():
    token = call_api_login()
    token = token.strip()
    url = f"{API_BASE}/api/v1/Tarefa/ListarTarefasPorUsuario"
    header = {
        "Accep": "*/*",
        "dsCliente" : "mobile",
        "dsChaveAutenticacao" : AUTENTICACAO,
        "tokenUsuario" : token,
        "CdProcesso" : "12"
    }
    response = requests.get(url, header=header)
    if response.status_code != 200:
        print("ERRO API:", response.status_code)
        print(response.text)
        

    return  {
    "status": response.status_code,
    "body": response.json() if response.text else {}
    }