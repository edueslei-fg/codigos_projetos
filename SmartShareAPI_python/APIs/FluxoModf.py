import requests, logging, os
from dotenv import load_dotenv
from APIs.load_dependencias import API_BASE, AUTENTICACAO
from APIs.API_Login import call_api_login

Email = "lorenzo.guedes@fgempreendimentos.com.br"

def pular_fluxo(CdFluxo):
    token = call_api_login()
    print(token)
    url = f"{API_BASE}/api/v1/Fluxo/AvancaFluxo"
    CdFluxo = str(CdFluxo).strip()
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdFluxo": str(CdFluxo),
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),
        "dsEmailExecutor": str(Email)
    }
    body = {
        "cdFluxo": str(CdFluxo),
        "dsEmailExecutor": f"{Email}"
    }
    print("CdFluxo enviado:", repr(CdFluxo), type(CdFluxo))

    response = requests.post(url, headers=header, json=body)
    if response.status_code != 200:
        print("ERRO API:", response.status_code)
        print(response.text)
        print(CdFluxo)
    return  {
    "status": response.status_code,
    "body": response.json() if response.text else {}
    }