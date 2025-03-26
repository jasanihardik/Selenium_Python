from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FileUploadPage(BasePage):
    """Page object for WebDriverUniversity File Upload page"""
    
    # Locators
    FILE_UPLOAD_INPUT = (By.ID, "myFile")
    SUBMIT_BUTTON = (By.ID, "submit-button")
    
    def __init__(self, driver):
        """Initialize the FileUploadPage object"""
        super().__init__(driver)
    
    def upload_file(self, file_path):
        """
        Upload a file
        
        Args:
            file_path: Path to the file to upload
            
        Returns:
            FileUploadPage: Self reference for method chaining
        """
        self.logger.info(f"Uploading file: {file_path}")
        upload_input = self.wait_for_element_visible(self.FILE_UPLOAD_INPUT)
        upload_input.send_keys(file_path)
        return self
    
    def click_submit(self):
        """
        Click the submit button
        
        Returns:
            FileUploadPage: Self reference for method chaining
        """
        self.logger.info("Clicking submit button")
        self.click(self.SUBMIT_BUTTON)
        return self
    
    def accept_alert(self):
        """
        Accept the alert that appears after file upload
        
        Returns:
            FileUploadPage: Self reference for method chaining
        """
        self.logger.info("Accepting alert")
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text 