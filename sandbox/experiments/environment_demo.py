import os

print("=" * 60)
print("Environment Variables")
print("=" * 60)

print(f"USERNAME: {os.getenv('USERNAME')}")
print(f"TEMP: {os.getenv('TEMP')}")
print(f"PATH exists: {'PATH' in os.environ}")

print()
print(f"Total environment variables: {len(os.environ)}")

print()
print("=" * 60)
print("Adding a Variable")
print("=" * 60)

os.environ["COLOR"] = "blue"

print(os.environ["COLOR"])
print(os.getenv("COLOR"))

print()
print("=" * 60)
print("Missing Variables")
print("=" * 60)

print("Using getenv():")
print(os.getenv("NOT_REAL"))

print()

print("Using os.environ[]:")

try:
    print(os.environ["NOT_REAL"])
except KeyError as e:
    print(f"Caught exception: {e}")

from pathlib import Path
from dotenv import load_dotenv

print()
print("=" * 60)
print("Loading .env")
print("=" * 60)

project_root = Path(__file__).resolve().parents[2]

env_file = project_root / ".env"

print(f"Found .env: {env_file.exists()}")

load_dotenv(env_file)

print()

print(f"APP_ENV = {os.getenv('APP_ENV')}")
print(f"DATABASE_URL = {os.getenv('DATABASE_URL')}")
print(f"LOG_LEVEL = {os.getenv('LOG_LEVEL')}")

print()
print("=" * 60)
print("Did load_dotenv modify os.environ?")
print("=" * 60)

print("APP_ENV" in os.environ)
print(os.environ["APP_ENV"])

print()
print("=" * 60)
print("Changing the Environment")
print("=" * 60)

os.environ["APP_ENV"] = "production"

print("APP_ENV =", os.getenv("APP_ENV"))