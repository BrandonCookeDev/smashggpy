import os
import dotenv
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR = BASE_DIR/'..'/'..'


def run_dotenv():
    dotenv.load_dotenv(dotenv_path=Path(ROOT_DIR, '.env'))

