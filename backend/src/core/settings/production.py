from .base import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(ENV_DIR, ".env.production"))
