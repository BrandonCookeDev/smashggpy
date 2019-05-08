import os
from pathlib import Path  
from dotenv import load_dotenv

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR = BASE_DIR/'..'/'..'

def dotenv():
	env_path = ROOT_DIR / '.env'
	load_dotenv(dotenv_path=env_path)

def flatten(l: list):
	flat_list = []
	for sublist in l:
		for item in sublist:
			flat_list.append(item)
	return flat_list
