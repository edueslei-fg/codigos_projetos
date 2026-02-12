import requests, logging, os
from dotenv import load_dotenv
from APIs.load_dependencias import API_BASE, API_CLIENT, AUTENTICACAO
from APIs.API_Login import call_api_login

def inserir_anexo(cdFluxo, cdTarefa, cdTipoAnexo, dsAnexo, caminho):
    token = call_api_login()
    url = f"{API_BASE}/api/v1/Anexo/InserirAnexo"

    nome_arquivo = os.path.basename(caminho)

    headers = {
        "Accept": "*/*",
        "dsCliente": f"{API_CLIENT}",
        "token": str(token),
        "dsChaveAutenticacao": f"{AUTENTICACAO}",
        "cdFluxo": str(cdFluxo),
        "cdTarefa": str(cdTarefa),
        "cdTipoAnexo": str(cdTipoAnexo),
        "dsAnexo": dsAnexo,
        "dsNomeArquivoOriginal": nome_arquivo,
        
    }
    response = requests.post(url, headers=headers)

    if response.status_code != 200:
        print("ERRO API:", response.status_code)
        print(response.text)
        print(cdFluxo)
        print(token)

    return  {
    "status": response.status_code,
    "body": response.json() if response.text else {}
    }
print("STATUS:", response.status_code)
print("RETORNO:", response.text)