import sys
import importlib

REQUIRED_LIBRARIES = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
    "numpy": "Numerical computing ready"
}


def check_dependencies():
    """Check if the required libraries are installed."""
    print("OPERATOR STATUS: Loading programs...")
    print("Checking dependencies:")

    missing = []

    for lib, description in REQUIRED_LIBRARIES.items():
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - {description}")
        except ImportError:
            print(f"[ERROR] {lib} not installed")
            missing.append(lib)

    if missing:
        print("\nMissing dependencies detected:")
        for lib in missing:
            print(f"  - {lib}")

        print("\nInstall with pip:")
        print("  pip install -r requirements.txt")

        print("\nOr install with Poetry:")
        print("  poetry install")

        return False

    return True


def detect_environment():
    """Detect and print the environment type."""
    print("\nDetecting environment...")

    if "poetry" in sys.executable.lower():
        print("Environment: Poetry virtual environment")
    elif sys.prefix != sys.base_prefix:
        print("Environment: pip / venv environment")
    else:
        print("Environment: System Python (no virtual environment)")


def analyze_matrix():
    """Analyze and visualize matrix data."""
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import requests

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = pd.DataFrame({
        "x": np.arange(1000),
        "y": np.random.randn(1000).cumsum()
    })

    response = requests.models.Response()
    response.status_code = 200

    print("Network module loaded. Status simulated:", response.status_code)

    plt.figure(figsize=(10, 5))
    plt.plot(data["x"], data["y"])
    plt.title("Matrix Data Simulation - Signal Trace")
    plt.grid(True)
    plt.savefig("matrix_analysis.png")

    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_dependencies():
        detect_environment()
        analyze_matrix()
    else:
        sys.exit(1)
