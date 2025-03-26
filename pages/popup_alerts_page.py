from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PopupAlertsPage(BasePage):
    """Page object for WebDriverUniversity Popup & Alerts page"""
    
    # Locators
    JAVASCRIPT_ALERT_BUTTON = (By.ID, "button1")
    MODAL_POPUP_BUTTON = (By.ID, "button2")
    AJAX_LOADER_BUTTON = (By.ID, "button3")
    JAVASCRIPT_CONFIRM_BOX_BUTTON = (By.ID, "button4")
    
    # Modal Locators
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")
    MODAL_BODY = (By.CSS_SELECTOR, ".modal-body")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer .btn")
    
    # Ajax Loader Locators
    AJAX_SPINNER = (By.CSS_SELECTOR, "div.ajax-loader")
    AJAX_LOADED_TEXT = (By.CSS_SELECTOR, "div.modal-body p")
    AJAX_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-footer .btn-default")
    
    def __init__(self, driver):
        """Initialize the PopupAlertsPage object"""
        super().__init__(driver)
    
    def click_javascript_alert_button(self):
        """
        Click on the JavaScript Alert button
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.JAVASCRIPT_ALERT_BUTTON)
        return self
    
    def click_modal_popup_button(self):
        """
        Click on the Modal Popup button
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.MODAL_POPUP_BUTTON)
        return self
    
    def click_ajax_loader_button(self):
        """
        Click on the AJAX Loader button
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.AJAX_LOADER_BUTTON)
        return self
    
    def click_javascript_confirm_box_button(self):
        """
        Click on the JavaScript Confirm Box button
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.JAVASCRIPT_CONFIRM_BOX_BUTTON)
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
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.MODAL_CLOSE_BUTTON)
        return self
    
    def wait_for_ajax_loader(self):
        """
        Wait for the AJAX loader to complete
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        # First, verify the spinner appears
        self.wait_for_element_visible(self.AJAX_SPINNER)
        
        # Then wait for it to disappear and content to load
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.AJAX_LOADED_TEXT)
        )
        return self
    
    def get_ajax_loaded_text(self):
        """
        Get the text that appears after AJAX load completes
        
        Returns:
            str: The loaded text
        """
        return self.wait_for_element_visible(self.AJAX_LOADED_TEXT).text
    
    def close_ajax_modal(self):
        """
        Close the AJAX modal
        
        Returns:
            PopupAlertsPage: Self reference for method chaining
        """
        self.click(self.AJAX_CLOSE_BUTTON)
        return self
    
    def is_modal_displayed(self):
        """
        Check if the modal is displayed
        
        Returns:
            bool: True if the modal is displayed, False otherwise
        """
        return self.is_element_displayed(self.MODAL_TITLE) 