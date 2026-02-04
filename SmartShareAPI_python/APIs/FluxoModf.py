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
    headers = {         
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdFluxo": str(CdFluxo), 
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),   
        "dsEmailExecutor": str(Email) 
    }
    print("FLUXO:", CdFluxo) 

    body = {         
      "cdFluxo":  str(CdFluxo),  
      "dsEmailExecutor": f"{Email}"     
    }
    response = requests.post(url, headers=headers, json=body)      
    print("STATUS:", response.status_code)     
    print("BODY:", response.text)                            
    response.raise_for_status()
    return response.text

 