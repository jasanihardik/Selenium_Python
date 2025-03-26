from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time
from datetime import datetime

class DatepickerPage(BasePage):
    """Page object for WebDriverUniversity Datepicker page"""
    
    # Locators
    DATEPICKER_INPUT = (By.ID, "datepicker")
    DATEPICKER_CONTAINER = (By.CSS_SELECTOR, ".datepicker-container")
    TODAY_BUTTON = (By.CSS_SELECTOR, ".datepicker-days .today")
    DATEPICKER_SWITCH = (By.CSS_SELECTOR, ".datepicker-switch")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".prev")
    
    def __init__(self, driver):
        """Initialize the DatepickerPage object"""
        super().__init__(driver)
    
    def open_datepicker(self):
        """
        Click on the datepicker input to open the datepicker
        
        Returns:
            DatepickerPage: Self reference for method chaining
        """
        self.logger.info("Opening datepicker")
        self.click(self.DATEPICKER_INPUT)
        return self
    
    def select_today(self):
        """
        Click the 'Today' button in the datepicker
        
        Returns:
            DatepickerPage: Self reference for method chaining
        """
        self.logger.info("Selecting today's date")
        self.click(self.TODAY_BUTTON)
        return self
    
    def select_date(self, day, month, year):
        """
        Select a specific date in the datepicker
        
        Args:
            day: Day to select (int)
            month: Month to select (1-12)
            year: Year to select (int)
            
        Returns:
            DatepickerPage: Self reference for method chaining
        """
        self.logger.info(f"Selecting date: {day}/{month}/{year}")
        self.click(self.DATEPICKER_INPUT)
        
        # Navigate to the correct year and month
        current_date = self.get_current_datepicker_date()
        current_month, current_year = current_date
        
        # Navigate to the correct year
        while int(current_year) != year:
            if int(current_year) < year:
                self.click(self.NEXT_BUTTON)
            else:
                self.click(self.PREV_BUTTON)
            current_date = self.get_current_datepicker_date()
            _, current_year = current_date
        
        # Navigate to the correct month
        while int(current_month) != month:
            if int(current_month) < month:
                self.click(self.NEXT_BUTTON)
            else:
                self.click(self.PREV_BUTTON)
            current_date = self.get_current_datepicker_date()
            current_month, _ = current_date
        
        # Select the day
        day_element = self.driver.find_element(By.XPATH, f"//td[contains(@class, 'day') and text()='{day}']")
        day_element.click()
        
        return self
    
    def get_current_datepicker_date(self):
        """
        Get the current month and year displayed in the datepicker
        
        Returns:
            tuple: (month, year) as strings
        """
        switch_text = self.wait_for_element_visible(self.DATEPICKER_SWITCH).text
        # Format: "Month Year" (e.g. "March 2025")
        parts = switch_text.split()
        month_name = parts[0]
        year = parts[1]
        
        # Convert month name to number
        month_number = datetime.strptime(month_name, '%B').month
        
        return (month_number, year)
    
    def get_selected_date(self):
        """
        Get the selected date from the input field
        
        Returns:
            str: The selected date in MM/DD/YYYY format
        """
        return self.wait_for_element_visible(self.DATEPICKER_INPUT).get_attribute("value")
    
    def enter_date_manually(self, date_string):
        """
        Enter a date manually in the datepicker input
        
        Args:
            date_string: Date in MM/DD/YYYY format
            
        Returns:
            DatepickerPage: Self reference for method chaining
        """
        self.logger.info(f"Entering date manually: {date_string}")
        input_element = self.wait_for_element_visible(self.DATEPICKER_INPUT)
        input_element.clear()
        input_element.send_keys(date_string)
        input_element.send_keys(Keys.RETURN)
        return self 