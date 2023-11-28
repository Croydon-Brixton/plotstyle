import os

# Path to the plotstyle directory
PLOTSTYLE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTSTYLE_DATA_DIR = os.path.join(PLOTSTYLE_DIR, "data")

# Constants for unit conversions
INCH_TO_CM = 2.54
CM_TO_INCH = 1.0 / INCH_TO_CM
INCH_TO_PT = 72.0
PT_TO_INCH = 1.0 / INCH_TO_PT
CM_TO_PT = CM_TO_INCH * INCH_TO_PT
PT_TO_CM = 1.0 / CM_TO_PT
