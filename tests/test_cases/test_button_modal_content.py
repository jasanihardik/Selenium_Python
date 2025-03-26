import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("ButtonModalContentTest")

def test_print_button_modal_content(driver):
    """Print the exact content of the button click modals"""
    logger.info("Starting test_print_button_modal_content")
    
    # Navigate to homepage and then to Button Clicks page
    home_page = HomePage(driver)
    home_page.open()
    button_page = home_page.click_button_clicks()
    
    # Test simple button
    button_page.click_simple_button()
    title = button_page.get_modal_title()
    body = button_page.get_modal_body()
    print(f"\nSIMPLE BUTTON MODAL TITLE: '{title}'")
    print(f"SIMPLE BUTTON MODAL BODY: '{body}'")
    button_page.close_modal()
    
    # No further testing as other buttons don't produce reliable modals
    
    logger.info("test_print_button_modal_content completed") 