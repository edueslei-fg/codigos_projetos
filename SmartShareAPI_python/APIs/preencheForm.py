import requests, logging, json, os      #|
from dotenv import load_dotenv          #| Importação de Bibliotecas.
import json    

load_dotenv()
API_BASE = os.getenv("API_BASE")            #|
API_CLIENT = os.getenv("API_CLIENT")        #|
USUARIO = os.getenv("USUARIO")              #| Extrai as informações do .env.
SENHA = os.getenv("SENHA")                  #|
AUTENTICACAO = os.getenv("AUTENTICACAO")    #|
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")

codFluxo = input("Código do Fluxo:")
codTarefa = input("Código da Tarefa:")
campoForms = input("Campo do formulário a ser modificado:")
novoValor = input("Novo valor no formulário:")

def Camp_formsPre():
    url = f"{API_BASE}/api/v1/Fluxo/PreencheCampoFormulario"
    files = {
        'dsUsuario': (None, 'root.fg'), #|Login Root FG.
        'dsSenha': (None, 'Fg@2025@')   #|
    }
    header = { 
        'Content-Type': "application/json",
        'Accept': "application/json",
        'dsCliente': f"{API_CLIENT}",
        'dsChaveAutenticacao': f"{AUTENTICACAO}"
        }

    body = {
            "cdFluxo": f"{codFluxo}",  
            "cdTarefa": f"{codTarefa}",  
            "cdCampoFormulario": f"{campoForms}",
            "dsValor": f"{novoValor}"
            }
    response = requests.post(url, headers=header, json=body)
    print("STATUS", response.status_code)
    print("BODY", response.text)
    print(response.request.headers)
    print(response.request.body)   
    response.raise_for_status()
    return response

print(Camp_formsPre())
    