import sys
import site
import os

def verify_envir():
    if (sys.prefix == sys.base_prefix):
        print("MATRIX STATUS: You're still plugged in\n")
        try: 
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")
            print("\nThen run this program again.")
        except Exception as e:
            print(f"Exception: {e}")

    else:
        try:
            print("MATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print("Package installation path:")
            print(f"{site.getsitepackages([sys.prefix])}\n")
        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    verify_envir()
