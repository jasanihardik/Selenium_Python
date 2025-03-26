from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccordionPage(BasePage):
    """Page object for WebDriverUniversity Accordion page"""
    
    # Locators
    MANUAL_TESTING_HEADING = (By.ID, "manual-testing-accordion")
    MANUAL_TESTING_CONTENT = (By.ID, "manual-testing-description")
    CUCUMBER_HEADING = (By.ID, "cucumber-accordion")
    CUCUMBER_CONTENT = (By.ID, "cucumber-testing-description")
    AUTOMATION_HEADING = (By.ID, "automation-accordion")
    AUTOMATION_CONTENT = (By.ID, "automation-testing-description")
    CLICK_HEADING = (By.ID, "click-accordion")
    CLICK_CONTENT = (By.ID, "timeout")
    LOADING_ICON = (By.CSS_SELECTOR, "div.dotcontainer")
    
    def __init__(self, driver):
        """Initialize the AccordionPage object"""
        super().__init__(driver)
    
    def click_manual_testing_heading(self):
        """
        Click on the Manual Testing accordion heading
        
        Returns:
            AccordionPage: Self reference for method chaining
        """
        self.click(self.MANUAL_TESTING_HEADING)
        return self
    
    def click_cucumber_heading(self):
        """
        Click on the Cucumber accordion heading
        
        Returns:
            AccordionPage: Self reference for method chaining
        """
        self.click(self.CUCUMBER_HEADING)
        return self
    
    def click_automation_heading(self):
        """
        Click on the Automation Testing accordion heading
        
        Returns:
            AccordionPage: Self reference for method chaining
        """
        self.click(self.AUTOMATION_HEADING)
        return self
    
    def click_heading_with_loader(self):
        """
        Click on the 'Click' accordion heading that shows a loader
        
        Returns:
            AccordionPage: Self reference for method chaining
        """
        self.click(self.CLICK_HEADING)
        # Wait for the content to be visible
        self.wait_for_element_visible(self.CLICK_CONTENT)
        return self
    
    def get_manual_testing_content(self):
        """
        Get the Manual Testing accordion content text
        
        Returns:
            str: Manual Testing content text
        """
        element = self.wait_for_element_visible(self.MANUAL_TESTING_CONTENT)
        return element.text
    
    def get_cucumber_content(self):
        """
        Get the Cucumber accordion content text
        
        Returns:
            str: Cucumber content text
        """
        element = self.wait_for_element_visible(self.CUCUMBER_CONTENT)
        return element.text
    
    def get_automation_content(self):
        """
        Get the Automation Testing accordion content text
        
        Returns:
            str: Automation Testing content text
        """
        element = self.wait_for_element_visible(self.AUTOMATION_CONTENT)
        return element.text
    
    def get_click_content(self):
        """
        Get the Click accordion content text
        
        Returns:
            str: Click accordion content text
        """
        element = self.wait_for_element_visible(self.CLICK_CONTENT)
        return element.text
    
    def is_content_visible(self, content_locator):
        """
        Check if accordion content is visible
        
        Args:
            content_locator: Locator for the content element
            
        Returns:
            bool: True if the content is visible, False otherwise
        """
        return self.is_element_displayed(content_locator) 