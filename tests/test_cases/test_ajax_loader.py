import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("AjaxLoaderTests")

class TestAjaxLoader:
    """Test the Ajax Loader functionality"""
    
    def test_ajax_loader(self, driver):
        """Test that the Ajax loader works and the button becomes clickable after loading"""
        logger.info("Starting test_ajax_loader")
        
        # Navigate to homepage and then to Ajax Loader page
        home_page = HomePage(driver)
        home_page.open()
        ajax_page = home_page.click_ajax_loader()
        
        # Wait for loader to disappear and click the button
        ajax_page.click_button_after_loader()
        
        # Verify the modal is displayed
        assert ajax_page.is_modal_displayed(), "Modal should be displayed after clicking the button"
        
        # Get and log the modal title and body for verification
        modal_title = ajax_page.get_modal_title()
        modal_body = ajax_page.get_modal_body()
        logger.info(f"Modal title: {modal_title}")
        logger.info(f"Modal body: {modal_body}")
        
        # Verify the modal content
        assert "Well Done For Waiting" in modal_title, f"Modal title should contain 'Well Done For Waiting', got '{modal_title}'"
        assert "The waiting game can be a tricky one" in modal_body, f"Modal body should mention 'The waiting game', got '{modal_body}'"
        
        # Close the modal
        ajax_page.close_modal()
        
        logger.info("test_ajax_loader completed successfully") 