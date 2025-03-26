import pytest
import os
from pages.home_page import HomePage
from utilities.logger import setup_logger
from utilities.screenshot_utils import take_screenshot

# Set up logger for this test module
logger = setup_logger("ButtonClicksScreenshotTest")

def test_button_clicks_screenshot(driver):
    """Take screenshots of the button clicks page to understand its structure"""
    logger.info("Starting test_button_clicks_screenshot")
    
    # Navigate to homepage and then to Button Clicks page
    home_page = HomePage(driver)
    home_page.open()
    button_page = home_page.click_button_clicks()
    
    # Take a screenshot of the initial page using the utility
    screenshot_path = take_screenshot(driver, "button_clicks_initial")
    logger.info(f"Saved initial screenshot to {screenshot_path}")
    
    logger.info("test_button_clicks_screenshot completed successfully") 