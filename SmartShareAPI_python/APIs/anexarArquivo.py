import requests, logging, os      
from dotenv import load_dotenv 

load_dotenv(dotenv_path=r"SmartShareAPI_python\APIs\.env");      
API_BASE = os.getenv("API_BASE")            
API_CLIENT = os.getenv("API_CLIENT")        
USUARIO = os.getenv("USUARIO")              
SENHA = os.getenv("SENHA")                  
AUTENTICACAO = os.getenv("AUTENTICACAO")    
TOKEN_CLIENT = os.getenv("TOKEN_CLIENT")  

def anexarArquivo():
    headers = {
                'dsCliente': API_CLIENT, 
                'dsChaveAutenticacao': AUTENTICACAO,
                'cdTarefa' : srt(cdTarefa),
                
               }    
