import pytest
import os
from pages.home_page import HomePage
from utilities.logger import setup_logger
from utilities.screenshot_utils import take_screenshot

# Set up logger for this test module
logger = setup_logger("HomepageScreenshotTest")

def test_homepage_screenshot(driver):
    """Take a screenshot of the homepage to see what elements are available"""
    logger.info("Starting test_homepage_screenshot")
    
    # Navigate to homepage
    home_page = HomePage(driver)
    home_page.open()
    
    # Take a screenshot of the homepage using the utility
    screenshot_path = take_screenshot(driver, "homepage")
    logger.info(f"Saved homepage screenshot to {screenshot_path}")
    
    # Log all available links
    available_links = home_page.get_all_links()
    for name, is_displayed in available_links.items():
        logger.info(f"Link '{name}' is displayed: {is_displayed}")
    
    logger.info("test_homepage_screenshot completed successfully") 