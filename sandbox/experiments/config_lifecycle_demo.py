import os
from pathlib import Path

from dotenv import load_dotenv


def print_state(
    stage: str,
    env_file: Path,
    app_env: str | None,
    config: dict[str, dict[str, str | None]],
) -> None:
    """Print the value stored at each configuration layer."""

    print()
    print("=" * 70)
    print(stage)
    print("=" * 70)

    print(f".env file:      {read_env_file_value(env_file, 'APP_ENV')}")
    print(f"os.environ:     {os.getenv('APP_ENV')}")
    print(f"local variable: {app_env}")
    print(f"config dict:    {config['environment']['name']}")


def read_env_file_value(env_file: Path, variable_name: str) -> str | None:
    """Read one variable directly from the .env file without loading it."""

    if not env_file.exists():
        return None

    for line in env_file.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()

        if not stripped_line or stripped_line.startswith("#"):
            continue

        key, separator, value = stripped_line.partition("=")

        if separator and key.strip() == variable_name:
            return value.strip()

    return None


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"

print(f"Project root: {PROJECT_ROOT}")
print(f".env path:    {ENV_FILE}")
print(f".env exists:  {ENV_FILE.exists()}")

# ---------------------------------------------------------------------
# Stage 1: Before loading .env
# ---------------------------------------------------------------------

app_env = None

config = {
    "environment": {
        "name": None,
    }
}

print_state(
    stage="Stage 1: Before load_dotenv()",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 2: Load .env into os.environ
# ---------------------------------------------------------------------

load_dotenv(ENV_FILE)

print_state(
    stage="Stage 2: After load_dotenv()",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 3: Copy the environment value into a local variable
# ---------------------------------------------------------------------

app_env = os.getenv("APP_ENV")

print_state(
    stage="Stage 3: After creating the local variable",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 4: Copy the local variable into the config dictionary
# ---------------------------------------------------------------------

config["environment"]["name"] = app_env

print_state(
    stage="Stage 4: After building the config dictionary",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 5: Change only the local variable
# ---------------------------------------------------------------------

app_env = "testing"

print_state(
    stage="Stage 5: After changing only the local variable",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 6: Change only the config dictionary
# ---------------------------------------------------------------------

config["environment"]["name"] = "production"

print_state(
    stage="Stage 6: After changing only the config dictionary",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 7: Change only os.environ
# ---------------------------------------------------------------------

os.environ["APP_ENV"] = "qa"

print_state(
    stage="Stage 7: After changing only os.environ",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)

# ---------------------------------------------------------------------
# Stage 8: Refresh the local variable and config dictionary
# ---------------------------------------------------------------------

app_env = os.getenv("APP_ENV")
config["environment"]["name"] = app_env

print_state(
    stage="Stage 8: After explicitly refreshing the copies",
    env_file=ENV_FILE,
    app_env=app_env,
    config=config,
)