import os
import re
import dotenv
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR = BASE_DIR/'..'/'..'
EVENT_SLUG_REGEX = re.compile('tournament/([\S]*)/event/([\S]*)')


def run_dotenv():
    dotenv.load_dotenv(dotenv_path=Path(ROOT_DIR, '.env'))


def get_tournament_from_event_slug(event_slug: str):
    match = EVENT_SLUG_REGEX.match(event_slug)
    groups = match.groups()
    if len(groups) > 0:
        return groups[0]


def get_event_from_event_slug(event_slug: str):
    match = EVENT_SLUG_REGEX.match(event_slug)
    groups = match.groups()
    if len(groups) > 1:
        return groups[1]
