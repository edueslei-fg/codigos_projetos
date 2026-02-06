import requests, logging, os      
from dotenv import load_dotenv 

load_dotenv(dotenv_path=r"SmartShareAPI_python\APIs\.env");      
API_BASE = os.getenv("API_BASE")            
API_CLIENT = os.getenv("API_CLIENT")        
USUARIO = os.getenv("USUARIO")              
SENHA = os.getenv("SENHA")                  
AUTENTICACAO = os.getenv("AUTENTICACAO")    
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")  


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
def inserir_anexo(CdFluxo, CdTarefa, cdTipoAnexo, dsAnexo, dsNomeArquivoOriginal):
    token = call_api_login()

    url = f"{API_BASE}/api/v1/Anexo/InserirAnexo"

    nome_arquivo = os.path.basename(dsNomeArquivoOriginal)

    headers = {
        "Accept": "application/json",
        "dsCliente": "mobile",
        "dsChaveAutenticacao": AUTENTICACAO,
        "cdFluxo": str(CdFluxo),
        "cdTarefa": str(CdTarefa),
        "cdTipoAnexo": str(cdTipoAnexo),
        "dsAnexo": dsAnexo,
        "dsNomeArquivoOriginal": dsNomeArquivoOriginal,
        "tokenUsuario": token
    }

    # NÃO colocar Content-Type aqui

    with open(dsNomeArquivoOriginal, "rb") as f:
        files = {
            "file": (nome_arquivo, f)
        }

        response = requests.post(url, headers=headers, files=files)

    print("STATUS:", response.status_code)
    print("RETORNO:", response.text)
