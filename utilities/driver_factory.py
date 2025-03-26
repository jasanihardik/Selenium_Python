from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT, WINDOW_SIZE, HEADLESS
import os

class DriverFactory:
    """
    Factory class for creating WebDriver instances with proper configuration
    """
    
    @staticmethod
    def get_driver(browser):
        """
        Initialize the WebDriver based on the browser specified
        
        Args:
            browser (str): Browser name - chrome, firefox, or edge
            
        Returns:
            WebDriver: An instance of the specified browser driver
        """
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if HEADLESS:
                options.add_argument("--headless")
            options.add_argument(f"--window-size={WINDOW_SIZE[0]},{WINDOW_SIZE[1]}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            
            # Use the manually downloaded ChromeDriver
            chrome_driver_path = os.path.expanduser("~/.webdriver/chromedriver")
            if os.path.exists(chrome_driver_path):
                driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=options)
            else:
                # Fallback to webdriver_manager
                from webdriver_manager.chrome import ChromeDriverManager
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if HEADLESS:
                options.add_argument("--headless")
            options.add_argument(f"--width={WINDOW_SIZE[0]}")
            options.add_argument(f"--height={WINDOW_SIZE[1]}")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
        elif browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            if HEADLESS:
                options.add_argument("--headless")
            options.add_argument(f"--window-size={WINDOW_SIZE[0]},{WINDOW_SIZE[1]}")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        
        else:
            raise Exception(f"Browser '{browser}' is not supported. Use chrome, firefox, or edge.")
        
        # Set timeouts
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        
        return driver 