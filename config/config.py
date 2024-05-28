from dotenv import load_dotenv
from os import getenv
from getpass import getuser

load_dotenv()

TOKEN = getenv("TOKEN")
DATABASE = f"/home/{getuser()}/.config/user_data.db"
