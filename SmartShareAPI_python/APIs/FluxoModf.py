import requests, logging, os      
from dotenv import load_dotenv                       

load_dotenv(dotenv_path=r"SmartShareAPI_python\APIs\.env");      
API_BASE = os.getenv("API_BASE")            
API_CLIENT = os.getenv("API_CLIENT")        
USUARIO = os.getenv("USUARIO")              
SENHA = os.getenv("SENHA")                  
AUTENTICACAO = os.getenv("AUTENTICACAO")    
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")   

Email = "lorenzo.guedes@fgempreendimentos.com.br"           

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

def pular_fluxo(CdFluxo):    
    token = call_api_login()
    url = f"{API_BASE}/api/v1/Fluxo/AvancaFluxo"   
    CdFluxo = str(CdFluxo).strip()
    header = {         
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdFluxo": f"{CdFluxo}", 
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),   
        "dsEmailExecutor": str(Email) 
    }

    body = {
        "cdFluxo": CdFluxo,
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

 