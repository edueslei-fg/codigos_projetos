import requests, logging, json, os, sys, time
import mimetypes
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_BASE = os.getenv("API_BASE")
API_CLIENT = os.getenv("API_CLIENT")
API_KEY = os.getenv("API_KEY")
COD_TAREFA = os.getenv("COD_PROCESSO")
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")
AUTENTICACAO = os.getenv("AUTENTICACAO")
OPCAO = 10;

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

token = call_api_login();

def call_avancar_Fluxo(token, COD_TAREFA):
    url=f"{API_BASE}";
    payload ="";
    headers = {
  'dsCliente': f'{API_CLIENT}/api/v2/Fluxo/AvancaFluxo',
  'dsChaveAutenticacao': f'{API_KEY}',
  'tokenUsuario': f'{token}',
  'cdTarefa': f'{COD_TAREFA}',
  'cdOpcao': f'{OPCAO}'

    };
    response = requests.request("POST", url, headers=headers, data=payload);
    return response;
