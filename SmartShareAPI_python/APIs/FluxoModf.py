import requests, logging, json, os      
from dotenv import load_dotenv          
import json                             
def processar_nome(CdFluxo):
    print("Recebido:", CdFluxo )
    return f"Olá {CdFluxo}, salvo com sucesso!"

load_dotenv();      
API_BASE = os.getenv("API_BASE")            
API_CLIENT = os.getenv("API_CLIENT")        
USUARIO = os.getenv("USUARIO")              
SENHA = os.getenv("SENHA")                  
AUTENTICACAO = os.getenv("AUTENTICACAO")    
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")    

cod_fluxo = processar_nome()#input("Qual o código do processo? : ")       
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

token = call_api_login()       
def pular_fluxo():    
    url = f"{API_BASE}/api/v1/Fluxo/AvancaFluxo"   
    headers = {         
        "Content-Type": "application/json",
        "Accept": "application/json",
        "dsCliente": "mobile",
        "cdFluxo": str(cod_fluxo), 
        "dsChaveAutenticacao": AUTENTICACAO,
        "tokenUsuario": str(token),   
        "dsEmailExecutor": str(Email) 
    }
    print("FLUXO:", cod_fluxo) 

    body = {         
      "cdFluxo":  str(cod_fluxo),  
      "dsEmailExecutor": f"{Email}"     
    }
    response = requests.post(url, headers=headers, json=body)      
    print("STATUS:", response.status_code)     
    print("BODY:", response.text)               
    print(response.request.headers)             
    print(response.request.body)                

    response.raise_for_status()
    return response

print(pular_fluxo()) 