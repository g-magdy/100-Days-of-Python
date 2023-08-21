import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get("APP_ID"))
print(os.getenv("API_KEY"))
print(os.getenv("BEARER_TOKEN"))
print(os.getenv("SHEET_ENDPOINT"))
