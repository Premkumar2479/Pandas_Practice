try:
    import pandas as pd
    print("pandas is installed:", pd.__version__)
except ImportError:
    print("pandas is not installed")


# Reusable check function

def check_pandas_installed():
    try:
        import pandas as pd
        return True, pd.__version__
    except ImportError:
        return False, None


installed, version = check_pandas_installed()
if installed:
    print(f"pandas is installed: {version}")
else:
    print("pandas is not installed")
