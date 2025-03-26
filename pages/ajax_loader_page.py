from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AjaxLoaderPage(BasePage):
    """Page object for WebDriverUniversity Ajax Loader page"""
    
    # Locators
    CLICK_ME_BUTTON = (By.ID, "button1")
    AJAX_LOADER_SPINNER = (By.CSS_SELECTOR, "div#loader")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")
    MODAL_BODY = (By.CSS_SELECTOR, ".modal-body")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer .btn")
    
    def __init__(self, driver):
        """Initialize the AjaxLoaderPage object"""
        super().__init__(driver)
    
    def wait_for_loader_to_disappear(self):
        """
        Wait for the Ajax loader spinner to disappear
        
        Returns:
            AjaxLoaderPage: Self reference for method chaining
        """
        self.logger.info("Waiting for Ajax loader to disappear")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.AJAX_LOADER_SPINNER)
        )
        return self
    
    def click_button_after_loader(self):
        """
        Wait for the loader to disappear and then click the button
        
        Returns:
            AjaxLoaderPage: Self reference for method chaining
        """
        self.logger.info("Clicking button after loader disappears")
        self.wait_for_loader_to_disappear()
        self.click(self.CLICK_ME_BUTTON)
        return self
    
    def is_modal_displayed(self):
        """
        Check if the modal is displayed
        
        Returns:
            bool: True if the modal is displayed, False otherwise
        """
        return self.is_element_displayed(self.MODAL_TITLE)
    
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
            AjaxLoaderPage: Self reference for method chaining
        """
        self.click(self.MODAL_CLOSE_BUTTON)
        return self 