import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("ModalContentTest")

def test_print_modal_content(driver):
    """Print the exact content of the modal title and body"""
    logger.info("Starting test_print_modal_content")
    
    # Navigate to homepage and then to Popup & Alerts page
    home_page = HomePage(driver)
    home_page.open()
    popup_page = home_page.click_popup_alerts()
    
    # Click the Modal Popup button
    popup_page.click_modal_popup_button()
    
    # Print the exact content
    title = popup_page.get_modal_title()
    body = popup_page.get_modal_body()
    
    print(f"MODAL TITLE: '{title}'")
    print(f"TITLE LENGTH: {len(title)}")
    print("TITLE CHAR CODES:", [ord(c) for c in title])
    print(f"MODAL BODY: '{body}'")
    
    # Test the 'in' operator directly
    test_string = "It's that Easy!!"
    contains_result = test_string in title
    print(f"TEST: '{test_string}' in '{title}' = {contains_result}")
    
    # Close the modal
    popup_page.close_modal()
    
    logger.info("test_print_modal_content completed") 