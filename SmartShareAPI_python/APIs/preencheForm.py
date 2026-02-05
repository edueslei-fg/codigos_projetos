import requests, logging, json, os      #|
from dotenv import load_dotenv          #| Importação de Bibliotecas.
import json    

load_dotenv(dotenv_path=r"SmartShareAPI_python\APIs\.env");  

API_BASE = os.getenv("API_BASE")            #|
API_CLIENT = os.getenv("API_CLIENT")        #|
USUARIO = os.getenv("USUARIO")              #| Extrai as informações do .env.
SENHA = os.getenv("SENHA")                  #|
AUTENTICACAO = os.getenv("AUTENTICACAO")    #|
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")

def Camp_formsPre(CdFluxo, CdTarefa, CdCampo, Valor):
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
            "cdFluxo": f"{CdFluxo}",  
            "cdTarefa": f"{CdTarefa}",  
            "cdCampoFormulario": f"{CdCampo}",
            "dsValor": f"{Valor}"
            }
    response = requests.post(url, headers=header, json=body)   
    if response.status_code != 200:
        print("ERRO API:", response.status_code)
        print(response.text)
    return response.text

    