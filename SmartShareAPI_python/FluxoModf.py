import requests, logging, json, os, sys, time
import mimetypes
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv();
API_BASE = os.getenv("API_BASE")
API_CLIENT = os.getenv("API_CLIENT")
API_KEY = os.getenv("API_KEY")
COD_TAREFA = os.getenv("COD_TAREFA")
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")
AUTENTICACAO = os.getenv("AUTENTICACAO")
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")

cod_fluxo = input("Qual o código do processo? : ")
cod_tarefa = input("Avançará qual tarefa? : ")
OPCAO = input("Opção:");

#Gera Token de acesso para a API SmartShare
def call_api_login():
    url = f"{API_BASE}/api/v2/Usuario/ValidarLogin"
    files = {
        'dsUsuario': (None, 'root.fg'),
        'dsSenha': (None, 'Fg@2025@')
    }
    headers = {'dsCliente': API_CLIENT, 'dsChaveAutenticacao': AUTENTICACAO}
    resp = requests.post(url, headers=headers, files=files)
    resp.raise_for_status()
    token = resp.json().get("tokenUsuario")
    logging.info("Login OK, token recebido")
    return token

token = call_api_login()

print(token)
def avanca_fluxo(token, cod_fluxo, cod_tarefa):
    url = f"{API_BASE}/api/v2/Fluxo/AvancaFluxo"
    payload = json.dumps({
        "lstCamposForm": [],
        "lstExecutores": [{"cdUsuario": 2}]
    })
    headers = {
        'dsCliente': API_CLIENT,
        'dsChaveAutenticacao': AUTENTICACAO,
        'tokenUsuario': f"{token}",
        'cdFluxo': cod_fluxo,
        'cdTarefa': cod_tarefa,
        'cdOpcao': OPCAO,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    print("Fluxo avançado com sucesso.")
response = avanca_fluxo(token, cod_fluxo, cod_tarefa)
print(response)