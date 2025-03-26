import pytest
import os
import tempfile
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("FileUploadTests")

class TestFileUpload:
    """Test the File Upload functionality"""
    
    def test_file_upload(self, driver):
        """Test uploading a file"""
        logger.info("Starting test_file_upload")
        
        # Create a temporary file to upload
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        try:
            temp_file.write(b'Test file content for upload test')
            temp_file.close()
            file_path = temp_file.name
            logger.info(f"Created temporary file: {file_path}")
            
            # Navigate to homepage and then to File Upload page
            home_page = HomePage(driver)
            home_page.open()
            file_upload_page = home_page.click_file_upload()
            
            # Upload the file and submit
            file_upload_page.upload_file(file_path)
            file_upload_page.click_submit()
            
            # Accept the alert and verify the message
            alert_text = file_upload_page.accept_alert()
            logger.info(f"Alert text: {alert_text}")
            
            assert "uploaded" in alert_text.lower(), f"Expected upload confirmation in alert, got: {alert_text}"
            
            logger.info("test_file_upload completed successfully")
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
                logger.info(f"Deleted temporary file: {temp_file.name}") 