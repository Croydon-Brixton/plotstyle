import os

__all__ = ["PLOTSTYLE_DIR", "PLOTSTYLE_DATA_DIR"]

# Path to the plotstyle directory
PLOTSTYLE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTSTYLE_DATA_DIR = os.path.join(PLOTSTYLE_DIR, "data")
