import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("TodoListScreenshotTest")

class TestTodoListScreenshot:
    """Test to capture a screenshot of the Todo List page"""
    
    def test_capture_todo_list_screenshot(self, driver):
        """Capture a screenshot of the Todo List page"""
        logger.info("Starting test_capture_todo_list_screenshot")
        
        # Navigate to homepage and then to Todo List page
        home_page = HomePage(driver)
        home_page.open()
        todo_page = home_page.click_to_do_list()
        
        # Take screenshot
        screenshot_path = todo_page.take_screenshot("todo_list_page")
        logger.info(f"Screenshot saved at: {screenshot_path}")
        
        logger.info("test_capture_todo_list_screenshot completed successfully") 