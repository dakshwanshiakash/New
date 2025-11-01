import os
import sys
from dotenv import load_dotenv

load_dotenv()

def get_env(name, default=None, required=False, var_type=str):
    """
    Smart ENV Getter:
    ✅ default value support
    ✅ required var check
    ✅ type conversion (int, list, bool)
    """
    value = os.getenv(name, default)

    if required and (value is None or value == ""):
        print(f"⚠️ ERROR: Missing required environment variable → {name}")
        sys.exit(1)

    try:
        if var_type == int:
            return int(value)
        elif var_type == list:
            return list(map(int, value.split()))
        elif var_type == bool:
            return value.lower() in ["true", "1", "yes", "on"]
        return value
    except Exception:
        print(f"⚠️ ERROR: Invalid value for {name}")
        sys.exit(1)


class Config:

    # ✅ Required (Without these bot can't run)
    API_ID = get_env("API_ID", required=True, var_type=int)
    API_HASH = get_env("API_HASH", required=True)
    BOT_TOKEN = get_env("BOT_TOKEN", required=True)

    # ✅ Owner & Permissions
    OWNER_ID = get_env("OWNER_ID", required=True, var_type=int)
    SUDO_USERS = get_env("SUDO_USERS", default="0", var_type=list)

    # ✅ MongoDB
    MONGO_DB_URI = get_env("MONGO_DB_URI", required=True)

    # ✅ Logging & Bot Info
    LOG_GROUP_ID = get_env("LOG_GROUP_ID", required=True, var_type=int)
    BOT_NAME = get_env("BOT_NAME", default="AnanyaMusic")

    # ✅ Music Settings / Energies
    DURATION_LIMIT = get_env("DURATION_LIMIT", default="300", var_type=int)
    COMMAND_PREFIXES = get_env("COMMAND_PREFIXES", default="! / . ?", var_type=list)

    # ✅ Userbot Session
    STRING_SESSION = get_env("STRING_SESSION", default=None)

    # ✅ Optional Deployment Info
    UPSTREAM_REPO = get_env("UPSTREAM_REPO", default="")
    UPSTREAM_BRANCH = get_env("UPSTREAM_BRANCH", default="main")

    # ✅ System Flags
    DEBUG_MODE = get_env("DEBUG_MODE", default="False", var_type=bool)
    AUTO_RESTART = get_env("AUTO_RESTART", default="True", var_type=bool)


config = Config()
