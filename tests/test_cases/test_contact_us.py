import pytest
from pages.home_page import HomePage
from tests.test_data.test_data import ContactFormData
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("ContactUsTests")

class TestContactUs:
    """Test the Contact Us functionality"""
    
    def test_successful_submission(self, driver):
        """Test that a user can successfully submit the contact form with valid data"""
        logger.info("Starting test_successful_submission")
        
        # Navigate to the homepage and then to the Contact Us page
        home_page = HomePage(driver)
        home_page.open()
        contact_page = home_page.click_contact_us()
        
        # Fill and submit the form
        data = ContactFormData.VALID_DATA
        contact_page.fill_contact_form(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["comment"]
        ).submit_form()
        
        # Verify the success message
        assert contact_page.is_form_submitted_successfully(), "Form was not submitted successfully"
        assert "thank you" in contact_page.get_success_message().lower(), "Success message not displayed correctly"
        
        logger.info("test_successful_submission completed successfully")
    
    def test_reset_form(self, driver):
        """Test that the reset button clears the form"""
        logger.info("Starting test_reset_form")
        
        # Navigate to the homepage and then to the Contact Us page
        home_page = HomePage(driver)
        home_page.open()
        contact_page = home_page.click_contact_us()
        
        # Fill the form and reset it
        data = ContactFormData.VALID_DATA
        contact_page.fill_contact_form(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["comment"]
        ).reset_form()
        
        # Verify the form is empty
        assert contact_page.is_form_reset(), "Form was not reset successfully"
        
        logger.info("test_reset_form completed successfully")
    
    def test_missing_email(self, driver):
        """Test form submission with missing email"""
        logger.info("Starting test_missing_email")
        
        # Navigate to the homepage and then to the Contact Us page
        home_page = HomePage(driver)
        home_page.open()
        contact_page = home_page.click_contact_us()
        
        # Fill and submit the form with missing email
        data = ContactFormData.MISSING_EMAIL_DATA
        contact_page.fill_contact_form(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["comment"]
        ).submit_form()
        
        # Verify error message
        assert "error" in contact_page.get_error_message().lower(), "Error message not displayed for missing email"
        
        logger.info("test_missing_email completed successfully")
    
    def test_missing_first_name(self, driver):
        """Test form submission with missing first name"""
        logger.info("Starting test_missing_first_name")
        
        # Navigate to the homepage and then to the Contact Us page
        home_page = HomePage(driver)
        home_page.open()
        contact_page = home_page.click_contact_us()
        
        # Fill and submit the form with missing first name
        data = ContactFormData.MISSING_FIRST_NAME_DATA
        contact_page.fill_contact_form(
            data["first_name"],
            data["last_name"],
            data["email"],
            data["comment"]
        ).submit_form()
        
        # Verify error message
        assert "error" in contact_page.get_error_message().lower(), "Error message not displayed for missing first name"
        
        logger.info("test_missing_first_name completed successfully") 