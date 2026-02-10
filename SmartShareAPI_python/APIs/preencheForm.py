import requests, logging, json, os
from dotenv import load_dotenv
import json
from APIs.load_dependencias import API_BASE, API_CLIENT, AUTENTICACAO

def Camp_formsPre(CdFluxo, CdTarefa, CdCampo, Valor):
    url = f"{API_BASE}/api/v1/Fluxo/PreencheCampoFormulario"
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
        print(CdFluxo)

    return  {
    "status": response.status_code,
    "body": response.json() if response.text else {}
    }