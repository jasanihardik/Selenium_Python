import pytest
import time
from pages.home_page import HomePage
from utilities.logger import setup_logger
from datetime import datetime, timedelta

# Set up logger for this test module
logger = setup_logger("DatepickerTests")

class TestDatepicker:
    """Test the Datepicker functionality"""
    
    def test_datepicker_navigation(self, driver):
        """Test basic navigation in the datepicker"""
        logger.info("Starting test_datepicker_navigation")
        
        # Navigate to homepage and then to Datepicker page
        home_page = HomePage(driver)
        home_page.open()
        datepicker_page = home_page.click_datepicker()
        
        # Open datepicker
        datepicker_page.open_datepicker()
        
        # Verify datepicker is displayed by checking the datepicker switch
        datepicker_switch = datepicker_page.wait_for_element_visible(datepicker_page.DATEPICKER_SWITCH)
        switch_text = datepicker_switch.text
        logger.info(f"Datepicker month/year: {switch_text}")
        
        # Click the next button and verify the month changes
        datepicker_page.click(datepicker_page.NEXT_BUTTON)
        
        # Wait a moment for the transition
        time.sleep(1)
        
        # Get the new month/year
        new_switch_text = datepicker_page.wait_for_element_visible(datepicker_page.DATEPICKER_SWITCH).text
        logger.info(f"New datepicker month/year: {new_switch_text}")
        
        # Verify the month changed
        assert switch_text != new_switch_text, f"Expected month to change from {switch_text}"
        
        logger.info("test_datepicker_navigation completed successfully") 