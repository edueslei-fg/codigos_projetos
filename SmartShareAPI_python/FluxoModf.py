import requests, logging, json, os, sys, time;
import mimetypes;
from dotenv import load_dotenv;

load_dotenv();

API_BASE = os.getenv("API_BASE");
