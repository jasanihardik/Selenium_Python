import os
import pytest
from datetime import datetime
from config.config import SCREENSHOTS_DIR

def take_screenshot(driver, test_name):
    """
    Take a screenshot and save it to the screenshots directory
    
    Args:
        driver: WebDriver instance
        test_name: Name of the test
        
    Returns:
        str: Path to the screenshot
    """
    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)
        
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
    
    driver.save_screenshot(screenshot_path)
    
    return screenshot_path

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to take screenshot when test fails
    
    Args:
        item: Test item
        call: Call info
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    
    # We only look at actual test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs["driver"]
            test_name = item.nodeid.replace("::", "_").replace("/", "_").replace(".py", "")
            screenshot_path = take_screenshot(driver, test_name)
            
            # Add screenshot to HTML report
            extra = getattr(rep, "extra", [])
            extra.append(pytest.html.extras.image(screenshot_path))
            rep.extra = extra
            
        except Exception as e:
            print(f"Failed to take screenshot: {e}") 