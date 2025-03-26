import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("AccordionTests")

class TestAccordion:
    """Test the Accordion functionality"""
    
    @pytest.mark.skip(reason="Accordion link is not available on the WebDriverUniversity homepage")
    def test_accordion_sections(self, driver):
        """Test that all accordion sections can be expanded and collapsed"""
        logger.info("Starting test_accordion_sections")
        
        # Navigate to homepage and then to Accordion page
        home_page = HomePage(driver)
        home_page.open()
        accordion_page = home_page.click_accordion()
        
        # Test Manual Testing section
        accordion_page.click_manual_testing_heading()
        manual_content = accordion_page.get_manual_testing_content()
        logger.info(f"Manual Testing content: {manual_content}")
        assert "Manual testing" in manual_content, "Manual Testing content not as expected"
        
        # Test Cucumber section
        accordion_page.click_cucumber_heading()
        cucumber_content = accordion_page.get_cucumber_content()
        logger.info(f"Cucumber content: {cucumber_content}")
        assert "Cucumber" in cucumber_content, "Cucumber content not as expected"
        
        # Test Automation section
        accordion_page.click_automation_heading()
        automation_content = accordion_page.get_automation_content()
        logger.info(f"Automation content: {automation_content}")
        assert "Automation" in automation_content, "Automation content not as expected"
        
        # Test section with loader
        accordion_page.click_heading_with_loader()
        loader_content = accordion_page.get_click_content()
        logger.info(f"Loader content: {loader_content}")
        assert "This text has appeared after" in loader_content, "Loader content not as expected"
        
        logger.info("test_accordion_sections completed successfully") 