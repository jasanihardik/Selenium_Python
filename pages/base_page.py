import os
import logging
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from config.config import EXPLICIT_WAIT, SCREENSHOTS_DIR
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    """
    Base page class that all page objects inherit from.
    Contains common methods for all pages.
    """
    
    def __init__(self, driver):
        """
        Initialize the BasePage class
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(
            driver, 
            EXPLICIT_WAIT, 
            poll_frequency=0.5,
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException
            ]
        )
        self.actions = ActionChains(driver)
        self.logger = self._setup_logger()
    
    def _setup_logger(self):
        """Set up the logger for the page object"""
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)
        return logger
    
    def navigate_to(self, url):
        """Navigate to the specified URL"""
        self.logger.info(f"Navigating to: {url}")
        self.driver.get(url)
    
    def get_title(self):
        """Get the page title"""
        return self.driver.title
    
    def get_url(self):
        """Get the current URL"""
        return self.driver.current_url
    
    def wait_for_element_visible(self, locator):
        """
        Wait for element to be visible
        
        Args:
            locator: (by, value) tuple
            
        Returns:
            WebElement: The element once it's visible
        """
        self.logger.info(f"Waiting for element to be visible: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        """
        Wait for element to be clickable
        
        Args:
            locator: (by, value) tuple
            
        Returns:
            WebElement: The element once it's clickable
        """
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_elements_visible(self, locator):
        """
        Wait for elements to be visible
        
        Args:
            locator: (by, value) tuple
            
        Returns:
            List[WebElement]: A list of visible elements
        """
        self.logger.info(f"Waiting for elements to be visible: {locator}")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click(self, locator):
        """
        Click on an element
        
        Args:
            locator: (by, value) tuple
        """
        self.logger.info(f"Clicking on element: {locator}")
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    def type_text(self, locator, text):
        """
        Type text into an element
        
        Args:
            locator: (by, value) tuple
            text: Text to type
        """
        self.logger.info(f"Typing '{text}' into element: {locator}")
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """
        Get text from an element
        
        Args:
            locator: (by, value) tuple
            
        Returns:
            str: Text content of the element
        """
        element = self.wait_for_element_visible(locator)
        text = element.text
        self.logger.info(f"Got text from element {locator}: '{text}'")
        return text
    
    def is_element_displayed(self, locator, timeout=5):
        """
        Check if element is displayed
        
        Args:
            locator: (by, value) tuple
            timeout: Time to wait for element
            
        Returns:
            bool: True if element is displayed, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        """
        Scroll to an element
        
        Args:
            locator: (by, value) tuple
        """
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def hover_over_element(self, locator):
        """
        Hover over an element
        
        Args:
            locator: (by, value) tuple
        """
        element = self.wait_for_element_visible(locator)
        self.actions.move_to_element(element).perform()
    
    def hover(self, locator):
        """
        Alias for hover_over_element
        
        Args:
            locator: (by, value) tuple
        """
        self.hover_over_element(locator)
    
    def take_screenshot(self, name=None):
        """
        Take a screenshot
        
        Args:
            name: Screenshot name (optional)
            
        Returns:
            str: Path to the screenshot
        """
        if not os.path.exists(SCREENSHOTS_DIR):
            os.makedirs(SCREENSHOTS_DIR)
            
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
        screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
        
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved: {screenshot_path}")
        
        return screenshot_path
    
    def switch_to_iframe(self, locator=None, iframe_index=None):
        """
        Switch to an iframe
        
        Args:
            locator: (by, value) tuple (optional)
            iframe_index: Index of the iframe (optional)
        """
        if locator:
            iframe = self.wait_for_element_visible(locator)
            self.driver.switch_to.frame(iframe)
        elif iframe_index is not None:
            self.driver.switch_to.frame(iframe_index)
        else:
            raise ValueError("Either locator or iframe_index must be provided")
    
    def switch_to_default_content(self):
        """Switch back to default content from iframe"""
        self.driver.switch_to.default_content()
    
    def switch_to_window(self, window_index=1):
        """
        Switch to a window by index
        
        Args:
            window_index: Index of the window to switch to (default is 1, the new window)
        """
        windows = self.driver.window_handles
        if window_index < len(windows):
            self.driver.switch_to.window(windows[window_index])
        else:
            raise ValueError(f"Window index {window_index} is out of range. Only {len(windows)} windows available.")
    
    def close_current_window(self):
        """Close current window and switch back to original window"""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def accept_alert(self):
        """Accept an alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self):
        """Dismiss an alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
    
    def get_alert_text(self):
        """
        Get text from an alert
        
        Returns:
            str: Text from the alert
        """
        alert = self.wait.until(EC.alert_is_present())
        return alert.text 