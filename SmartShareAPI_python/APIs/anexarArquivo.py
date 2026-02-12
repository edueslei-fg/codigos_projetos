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
        "dsCliente": API_CLIENT,
        "tokenUsuario": str(token),
        "dsChaveAutenticacao": AUTENTICACAO,
        "cdFluxo": str(cdFluxo),
        "cdTarefa": str(cdTarefa),
        "cdTipoAnexo": str(cdTipoAnexo),
        "dsAnexo": dsAnexo,
        "dsNomeArquivoOriginal": nome_arquivo,
    }

    with open(caminho, "rb") as f:
        files = {
            "file": (nome_arquivo, f)
        }

        response = requests.post(url, headers=headers, files=files)

    print("STATUS:", response.status_code)
    print("RETORNO:", response.text)
    print(response.request.headers)
    print(response.request.body[:500])

    return {
        "status": response.status_code,
        "body": response.json() if response.text else {}
    }
