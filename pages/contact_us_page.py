from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    """Page object for the WebDriverUniversity Contact Us page"""
    
    # Locators
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='last_name']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    COMMENTS_FIELD = (By.CSS_SELECTOR, "textarea[name='message']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[value='SUBMIT']")
    RESET_BUTTON = (By.CSS_SELECTOR, "input[value='RESET']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#contact_reply h1")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "body")
    
    def __init__(self, driver):
        """Initialize the ContactUsPage object"""
        super().__init__(driver)
    
    def fill_contact_form(self, first_name, last_name, email, comment):
        """
        Fill the contact form with the provided data
        
        Args:
            first_name: First name
            last_name: Last name
            email: Email address
            comment: Comment/message
            
        Returns:
            ContactUsPage: Self reference for method chaining
        """
        self.type_text(self.FIRST_NAME_FIELD, first_name)
        self.type_text(self.LAST_NAME_FIELD, last_name)
        self.type_text(self.EMAIL_FIELD, email)
        self.type_text(self.COMMENTS_FIELD, comment)
        return self
    
    def submit_form(self):
        """
        Submit the contact form
        
        Returns:
            ContactUsPage: Self reference for method chaining
        """
        self.click(self.SUBMIT_BUTTON)
        return self
    
    def reset_form(self):
        """
        Reset the contact form
        
        Returns:
            ContactUsPage: Self reference for method chaining
        """
        self.click(self.RESET_BUTTON)
        return self
    
    def get_success_message(self):
        """
        Get the success message text after form submission
        
        Returns:
            str: Success message text
        """
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def get_error_message(self):
        """
        Get the error message text after form submission
        
        Returns:
            str: Error message text
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_form_submitted_successfully(self):
        """
        Check if the form was submitted successfully
        
        Returns:
            bool: True if submission was successful, False otherwise
        """
        return self.is_element_displayed(self.SUCCESS_MESSAGE)
    
    def is_form_reset(self):
        """
        Check if the form was reset
        
        Returns:
            bool: True if form is empty, False otherwise
        """
        first_name = self.wait_for_element_visible(self.FIRST_NAME_FIELD).get_attribute("value")
        last_name = self.wait_for_element_visible(self.LAST_NAME_FIELD).get_attribute("value")
        email = self.wait_for_element_visible(self.EMAIL_FIELD).get_attribute("value")
        comments = self.wait_for_element_visible(self.COMMENTS_FIELD).get_attribute("value")
        
        return first_name == "" and last_name == "" and email == "" and comments == "" 