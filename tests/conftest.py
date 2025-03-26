import pytest
import os
from datetime import datetime
from selenium import webdriver
from config.config import BROWSER, REPORTS_DIR, REPORT_NAME
from utilities.driver_factory import DriverFactory
from utilities.logger import setup_logger
from py.xml import html

# Set up logger
logger = setup_logger("TestSetup")

def pytest_addoption(parser):
    """Add command line options for pytest"""
    parser.addoption("--browser-name", action="store", default=BROWSER,
                     help="Browser to run tests on: chrome, firefox, or edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run browser in headless mode")

@pytest.fixture(scope="session")
def driver_init(request):
    """
    Fixture to initialize WebDriver for the test session
    
    Args:
        request: Pytest request object
        
    Returns:
        WebDriver: WebDriver instance
    """
    browser = request.config.getoption("--browser-name")
    logger.info(f"Starting test session with {browser} browser")
    
    # Initialize the driver
    driver = DriverFactory.get_driver(browser)
    
    # Yield driver to the test
    yield driver
    
    # Quit the driver after the test
    logger.info("Closing browser after test session")
    driver.quit()

@pytest.fixture
def driver(driver_init, request):
    """
    Fixture to get WebDriver for a single test
    
    Args:
        driver_init: Session-scoped WebDriver
        request: Pytest request object
        
    Returns:
        WebDriver: WebDriver instance
    """
    driver = driver_init
    
    # Set up test name for logging
    test_name = request.node.name
    logger.info(f"Starting test: {test_name}")
    
    # Return driver to the test
    yield driver
    
    # Log after test
    logger.info(f"Finished test: {test_name}")

def pytest_configure(config):
    """Configure pytest with report settings"""
    # Create reports directory if it doesn't exist
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
    
    # Configure HTML report
    config.option.htmlpath = os.path.join(REPORTS_DIR, REPORT_NAME)
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    """Set the title of the HTML report"""
    report.title = "Automation Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Add description to HTML report
    
    Args:
        item: Test item
        call: Call info
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        # Add test docstring to the report
        doc = getattr(item.function, "__doc__", None)
        if doc:
            report.description = doc.strip() 