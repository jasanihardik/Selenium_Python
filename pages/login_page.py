from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page object for the WebDriverUniversity Login Portal page"""
    
    # Locators
    USERNAME_FIELD = (By.CSS_SELECTOR, "#text")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    
    def __init__(self, driver):
        """Initialize the LoginPage object"""
        super().__init__(driver)
    
    def login(self, username, password):
        """
        Login with the provided credentials
        
        Args:
            username: Username to login with
            password: Password to login with
        """
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_alert_text(self):
        """
        Get the text from the alert
        
        Returns:
            str: Alert text
        """
        return super().get_alert_text()
    
    def accept_alert(self):
        """Accept the alert"""
        super().accept_alert()
        
    def is_success_message_displayed(self):
        """
        Check if the success message is displayed
        
        Returns:
            bool: True if message is "validation succeeded", False otherwise
        """
        try:
            alert_text = self.get_alert_text()
            return "validation succeeded" in alert_text.lower()
        except:
            return False
    
    def is_error_message_displayed(self):
        """
        Check if the error message is displayed
        
        Returns:
            bool: True if message is "validation failed", False otherwise
        """
        try:
            alert_text = self.get_alert_text()
            return "validation failed" in alert_text.lower()
        except:
            return False 