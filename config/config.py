import os
from datetime import datetime

# Base URL for the application
BASE_URL = "https://webdriveruniversity.com/"

# Browser options
BROWSER = "chrome"  # chrome, firefox, edge
HEADLESS = False
WINDOW_SIZE = (1920, 1080)

# Timeouts in seconds
IMPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30
EXPLICIT_WAIT = 20

# Test data
TEST_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "test_data")

# Reports
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# Create a timestamp for report names
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

REPORT_NAME = f"test_report_{get_timestamp()}.html" 