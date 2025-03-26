from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ButtonClicksPage(BasePage):
    """Page object for WebDriverUniversity Button Clicks page"""
    
    # Locators
    SIMPLE_BUTTON = (By.ID, "button1")
    ACTION_MOVE_BUTTON = (By.ID, "button2")
    ACTION_CLICK_BUTTON = (By.ID, "button3")
    
    # Modal Locators
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")
    MODAL_BODY = (By.CSS_SELECTOR, ".modal-body")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer .btn")
    
    def __init__(self, driver):
        """Initialize the ButtonClicksPage object"""
        super().__init__(driver)
    
    def click_simple_button(self):
        """
        Click on the Simple Button
        
        Returns:
            ButtonClicksPage: Self reference for method chaining
        """
        self.click(self.SIMPLE_BUTTON)
        return self
    
    def hover_action_move_button(self):
        """
        Hover over the Action Move Button
        
        Returns:
            ButtonClicksPage: Self reference for method chaining
        """
        self.hover(self.ACTION_MOVE_BUTTON)
        return self
    
    def click_action_click_button(self):
        """
        Click on the Action Click Button
        
        Returns:
            ButtonClicksPage: Self reference for method chaining
        """
        self.click(self.ACTION_CLICK_BUTTON)
        return self
    
    def get_modal_title(self):
        """
        Get the modal title text
        
        Returns:
            str: Modal title text
        """
        return self.wait_for_element_visible(self.MODAL_TITLE).text
    
    def get_modal_body(self):
        """
        Get the modal body text
        
        Returns:
            str: Modal body text
        """
        return self.wait_for_element_visible(self.MODAL_BODY).text
    
    def close_modal(self):
        """
        Close the modal
        
        Returns:
            ButtonClicksPage: Self reference for method chaining
        """
        self.click(self.MODAL_CLOSE_BUTTON)
        return self
    
    def is_modal_displayed(self):
        """
        Check if the modal is displayed
        
        Returns:
            bool: True if the modal is displayed, False otherwise
        """
        return self.is_element_displayed(self.MODAL_TITLE) 