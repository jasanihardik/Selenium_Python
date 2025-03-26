import pytest
from pages.home_page import HomePage
from tests.test_data.test_data import LoginData
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("LoginTests")

class TestLogin:
    """Test the Login Portal functionality"""
    
    def test_successful_login(self, driver):
        """Test that a user can successfully login with valid credentials"""
        logger.info("Starting test_successful_login")
        
        # Navigate to the homepage and then to the Login Portal page
        home_page = HomePage(driver)
        home_page.open()
        login_page = home_page.click_login_portal()
        
        # Login with valid credentials
        credentials = LoginData.VALID_CREDENTIALS
        login_page.login(credentials["username"], credentials["password"])
        
        # Verify the success message and dismiss the alert
        assert login_page.is_success_message_displayed(), "Success message not displayed after valid login"
        login_page.accept_alert()
        
        logger.info("test_successful_login completed successfully")
    
    def test_failed_login(self, driver):
        """Test that a user cannot login with invalid credentials"""
        logger.info("Starting test_failed_login")
        
        # Navigate to the homepage and then to the Login Portal page
        home_page = HomePage(driver)
        home_page.open()
        login_page = home_page.click_login_portal()
        
        # Login with invalid credentials
        credentials = LoginData.INVALID_CREDENTIALS
        login_page.login(credentials["username"], credentials["password"])
        
        # Verify the error message and dismiss the alert
        assert login_page.is_error_message_displayed(), "Error message not displayed after invalid login"
        login_page.accept_alert()
        
        logger.info("test_failed_login completed successfully")
    
    def test_empty_credentials(self, driver):
        """Test that a user cannot login with empty credentials"""
        logger.info("Starting test_empty_credentials")
        
        # Navigate to the homepage and then to the Login Portal page
        home_page = HomePage(driver)
        home_page.open()
        login_page = home_page.click_login_portal()
        
        # Login with empty credentials
        credentials = LoginData.EMPTY_CREDENTIALS
        login_page.login(credentials["username"], credentials["password"])
        
        # Verify the error message and dismiss the alert
        assert login_page.is_error_message_displayed(), "Error message not displayed after empty login"
        login_page.accept_alert()
        
        logger.info("test_empty_credentials completed successfully")
    
    def test_username_only(self, driver):
        """Test that a user cannot login with only a username"""
        logger.info("Starting test_username_only")
        
        # Navigate to the homepage and then to the Login Portal page
        home_page = HomePage(driver)
        home_page.open()
        login_page = home_page.click_login_portal()
        
        # Login with only username
        credentials = LoginData.USERNAME_ONLY
        login_page.login(credentials["username"], credentials["password"])
        
        # Verify the error message and dismiss the alert
        assert login_page.is_error_message_displayed(), "Error message not displayed after username-only login"
        login_page.accept_alert()
        
        logger.info("test_username_only completed successfully")
    
    def test_password_only(self, driver):
        """Test that a user cannot login with only a password"""
        logger.info("Starting test_password_only")
        
        # Navigate to the homepage and then to the Login Portal page
        home_page = HomePage(driver)
        home_page.open()
        login_page = home_page.click_login_portal()
        
        # Login with only password
        credentials = LoginData.PASSWORD_ONLY
        login_page.login(credentials["username"], credentials["password"])
        
        # Verify the error message and dismiss the alert
        assert login_page.is_error_message_displayed(), "Error message not displayed after password-only login"
        login_page.accept_alert()
        
        logger.info("test_password_only completed successfully") 