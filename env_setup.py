import subprocess
import sys
import importlib.metadata

def ensure_requirements_installed(requirements_path="requirements.txt"):
    """
    Ensures all packages listed in requirements.txt are installed.
    Uses importlib.metadata instead of deprecated pkg_resources.
    """
    # Step 1: Parse requirements.txt
    try:
        with open(requirements_path, "r") as f:
            required_pkgs = {
                line.strip().split("==")[0].lower()
                for line in f if line.strip() and not line.startswith("#")
            }
    except FileNotFoundError:
        print(f"File not found: {requirements_path}")
        sys.exit(1)

    # Step 2: Get installed packages
    installed_pkgs = {
        dist.metadata["Name"].lower()
        for dist in importlib.metadata.distributions()
    }

    # Step 3: Install missing packages
    missing = required_pkgs - installed_pkgs
    if missing:
        print("Missing packages detected:")
        for pkg in missing:
            print(f" - {pkg}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        print("All missing packages installed.")
    else:
        print("All required packages are already installed.")
