import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

page = str(os.getenv('PAGE'))
user_agent = os.getenv('USER-AGENT')
