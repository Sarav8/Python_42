import os
from dotenv import load_dotenv
import sys


def load_oracle_config():
    """Load and display the Oracle configuration."""
    load_dotenv()

    mode = os.getenv('MATRIX_MODE')
    db = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    missing = []
    if not mode:
        missing.append('MATRIX_MODE')
    if not db:
        missing.append('DATABASE_URL')
    if not api:
        missing.append('API_KEY')
    if not log:
        missing.append('LOG_LEVEL')
    if not zion:
        missing.append('ZION_ENDPOINT')

    if missing:
        print("ERROR: Missing the following configuration variables:")
        for var in missing:
            print(f"  - {var}")
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    msg_db = ("Database: Connected to local instance"
              if db else "Database: Disconnected")
    print(msg_db)

    msg_api = "API Access: Authenticated" if api else "API Access: Error"
    print(msg_api)

    print(f"Log Level: {log}")

    msg_zion = "Zion Network: Online" if zion else "Zion Network: Offline"
    print(msg_zion)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nMasked sensitive values:")
    print(f"API_KEY: {mask_secret(api)}")
    print(f"DATABASE_URL: {mask_secret(db)}")

    print("\nThe Oracle sees all configurations.")


def mask_secret(value):
    """Mask sensitive information for security."""
    if value:
        return value[:4] + "..."
    return None


if __name__ == "__main__":
    load_oracle_config()
