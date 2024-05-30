from dotenv import load_dotenv
from os import getenv
from getpass import getuser

load_dotenv()

TOKEN: str = getenv("TOKEN")
DATABASE: str = f"/home/{getuser()}/.config/user_data.db"
TEST_DATABASE: str = f"/home/{getuser()}/.config/test_user_data.db"
TIMEOUT_CHECK_NOTIFY_USER: int = 30
