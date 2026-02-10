import requests, logging, os
from dotenv import load_dotenv
from APIs.load_dependencias import API_BASE, API_CLIENT, AUTENTICACAO

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
def inserir_anexo(CdFluxo, CdTarefa, cd_Tipo_Anexo, ds_Anexo, file_path):
    token = call_api_login()

    url = f"{API_BASE}/api/v1/Anexo/InserirAnexo"

    nome_arquivo = os.path.basename(file_path)

    headers = {
        "Accept": "*/*",
        "dsCliente": "mobile",
        "tokenUsuario": token,
        "dsChaveAutenticacao": AUTENTICACAO,
        "cdFluxo": str(CdFluxo),
        "cdTarefa": str(CdTarefa),
        "cdTipoAnexo": str(cd_Tipo_Anexo),
        "dsAnexo": ds_Anexo,
        "dsNomeArquivoOriginal": file_path,
        
    }
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, "rb") as f:
        files = (os.path.basename(file_path), f, "application/pdf")
        response = requests.post(url, headers=headers, files=files, timeout=60)
        response.raise_for_status()

    print("STATUS:", response.status_code)
    print("RETORNO:", response.text)