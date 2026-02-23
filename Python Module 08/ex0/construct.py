import sys
import os
import site


def check_matrix_status():
    """
    Detects if the script is running inside a virtual environment
    and displays relevant information about the Python environment.
    """
    try:
        in_venv = sys.prefix != sys.base_prefix

        if not in_venv:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows")
            print("\nThen run this program again.")
        else:
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")
            venv_name = os.path.basename(sys.prefix)
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            site_pack = site.getsitepackages([sys.prefix])[0]
            print(f"\nPackage installation path:\n{site_pack}")

    except Exception as e:
        print(f"Error accessing the Matrix: {e}")


if __name__ == "__main__":
    check_matrix_status()
