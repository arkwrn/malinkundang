from chaos_python.client import chaosAPI as chaosapi
from decouple import config

AMASS_API_KEY = config('AMASS_API_KEY')
	
def chaos_client(domain, options):
	return chaosapi(domain, AMASS_API_KEY, 'json')