import os
from dotenv import load_dotenv
from chaos_python.client import chaosAPI as chaosapi
load_dotenv()

AMASS_API_KEY = os.getenv('AMASS_API_KEY')
	
def chaos_client(domain, options):
	return chaosapi(domain, AMASS_API_KEY, 'json')