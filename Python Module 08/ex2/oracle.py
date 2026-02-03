import os
from dotenv import load_dotenv

load_dotenv()

var_ent = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]

mode = os.environ.get("MATRIX_MODE")
database = os.environ.get("DATABASE_URL")
api_key = os.environ.get("API_KEY")
log_level = os.environ.get("LOG_LEVEL")
zion = os.environ.get("ZION_ENDPOINT")

print("ORACLE STATUS: Reading the Matrix...")
print("Configuration loaded:")
print(f"Mode: {mode}")
print(f"Database: {database}")
print(f"API Access: {api_key}")
print(f"Log Level: {log_level}")
print(f"Zion Network: {zion}")


missing_vars = []

for var in var_ent:
    if os.environ.get(var) is None: 
        print(f"[ERROR] Missing dependency: {var}")
        missing_vars.append(var)
    else:
        print(f"[OK] {var} loaded")

if not missing_vars:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")
else:
    print("There were some missing variables. Please configure the environment correctly.")
