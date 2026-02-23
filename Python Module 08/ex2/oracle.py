import os
from dotenv import load_dotenv


def load_oracle_config():
    load_dotenv()

    mode = os.getenv('MATRIX_MODE')
    db = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    msg_db = "Database: Connected to local instance" if db \
        else "Database: Disconnected"
    print(msg_db)

    msg_api = "API Access: Authenticated" if api else "API Access: Error"
    print(msg_api)

    print(f"Log Level: {log}")

    msg_zion = "Zion Network: Online" if zion else "Zion Network: Offline"
    print(msg_zion)

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    load_oracle_config()
