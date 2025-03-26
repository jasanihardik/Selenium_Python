from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    """Page object for WebDriverUniversity Dropdown, Checkboxes & Radio Buttons page"""
    
    # Dropdown Locators
    DROPDOWN_MENU_1 = (By.ID, "dropdowm-menu-1")
    DROPDOWN_MENU_2 = (By.ID, "dropdowm-menu-2")
    DROPDOWN_MENU_3 = (By.ID, "dropdowm-menu-3")
    
    # Checkbox Locators
    CHECKBOX_1 = (By.CSS_SELECTOR, "input[value='option-1']")
    CHECKBOX_2 = (By.CSS_SELECTOR, "input[value='option-2']")
    CHECKBOX_3 = (By.CSS_SELECTOR, "input[value='option-3']")
    CHECKBOX_4 = (By.CSS_SELECTOR, "input[value='option-4']")
    
    # Radio Button Locators
    RADIO_BLUE = (By.CSS_SELECTOR, "input[value='blue']")
    RADIO_ORANGE = (By.CSS_SELECTOR, "input[value='orange']")
    RADIO_PURPLE = (By.CSS_SELECTOR, "input[value='purple']")
    RADIO_YELLOW = (By.CSS_SELECTOR, "input[value='yellow']")
    
    # Disabled elements locators
    RADIO_CABBAGE = (By.CSS_SELECTOR, "input[value='cabbage']")
    RADIO_PUMPKIN = (By.CSS_SELECTOR, "input[value='pumpkin']")
    
    def __init__(self, driver):
        """Initialize the DropdownPage object"""
        super().__init__(driver)
    
    def select_dropdown_value(self, dropdown_number, value):
        """
        Select a value from a dropdown menu
        
        Args:
            dropdown_number: Dropdown number (1-3)
            value: Value to select
            
        Returns:
            DropdownPage: Self reference for method chaining
        """
        if dropdown_number == 1:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_1)
        elif dropdown_number == 2:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_2)
        elif dropdown_number == 3:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_3)
        else:
            raise ValueError(f"Invalid dropdown number: {dropdown_number}")
        
        select = Select(dropdown)
        select.select_by_visible_text(value)
        return self
    
    def get_dropdown_selected_value(self, dropdown_number):
        """
        Get the currently selected value from a dropdown menu
        
        Args:
            dropdown_number: Dropdown number (1-3)
            
        Returns:
            str: Selected value
        """
        if dropdown_number == 1:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_1)
        elif dropdown_number == 2:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_2)
        elif dropdown_number == 3:
            dropdown = self.wait_for_element_visible(self.DROPDOWN_MENU_3)
        else:
            raise ValueError(f"Invalid dropdown number: {dropdown_number}")
        
        select = Select(dropdown)
        return select.first_selected_option.text
    
    def check_checkbox(self, checkbox_number):
        """
        Check a checkbox
        
        Args:
            checkbox_number: Checkbox number (1-4)
            
        Returns:
            DropdownPage: Self reference for method chaining
        """
        if checkbox_number == 1:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_1)
        elif checkbox_number == 2:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_2)
        elif checkbox_number == 3:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_3)
        elif checkbox_number == 4:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_4)
        else:
            raise ValueError(f"Invalid checkbox number: {checkbox_number}")
        
        if not checkbox.is_selected():
            checkbox.click()
        return self
    
    def uncheck_checkbox(self, checkbox_number):
        """
        Uncheck a checkbox
        
        Args:
            checkbox_number: Checkbox number (1-4)
            
        Returns:
            DropdownPage: Self reference for method chaining
        """
        if checkbox_number == 1:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_1)
        elif checkbox_number == 2:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_2)
        elif checkbox_number == 3:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_3)
        elif checkbox_number == 4:
            checkbox = self.wait_for_element_clickable(self.CHECKBOX_4)
        else:
            raise ValueError(f"Invalid checkbox number: {checkbox_number}")
        
        if checkbox.is_selected():
            checkbox.click()
        return self
    
    def is_checkbox_checked(self, checkbox_number):
        """
        Check if a checkbox is checked
        
        Args:
            checkbox_number: Checkbox number (1-4)
            
        Returns:
            bool: True if checked, False otherwise
        """
        if checkbox_number == 1:
            checkbox = self.wait_for_element_visible(self.CHECKBOX_1)
        elif checkbox_number == 2:
            checkbox = self.wait_for_element_visible(self.CHECKBOX_2)
        elif checkbox_number == 3:
            checkbox = self.wait_for_element_visible(self.CHECKBOX_3)
        elif checkbox_number == 4:
            checkbox = self.wait_for_element_visible(self.CHECKBOX_4)
        else:
            raise ValueError(f"Invalid checkbox number: {checkbox_number}")
        
        return checkbox.is_selected()
    
    def select_radio_button(self, color):
        """
        Select a radio button by color
        
        Args:
            color: Color of the radio button ('blue', 'orange', 'purple', 'yellow')
            
        Returns:
            DropdownPage: Self reference for method chaining
        """
        if color.lower() == 'blue':
            radio = self.wait_for_element_clickable(self.RADIO_BLUE)
        elif color.lower() == 'orange':
            radio = self.wait_for_element_clickable(self.RADIO_ORANGE)
        elif color.lower() == 'purple':
            radio = self.wait_for_element_clickable(self.RADIO_PURPLE)
        elif color.lower() == 'yellow':
            radio = self.wait_for_element_clickable(self.RADIO_YELLOW)
        else:
            raise ValueError(f"Invalid radio button color: {color}")
        
        radio.click()
        return self
    
    def is_radio_button_selected(self, color):
        """
        Check if a radio button is selected
        
        Args:
            color: Color of the radio button ('blue', 'orange', 'purple', 'yellow')
            
        Returns:
            bool: True if selected, False otherwise
        """
        if color.lower() == 'blue':
            radio = self.wait_for_element_visible(self.RADIO_BLUE)
        elif color.lower() == 'orange':
            radio = self.wait_for_element_visible(self.RADIO_ORANGE)
        elif color.lower() == 'purple':
            radio = self.wait_for_element_visible(self.RADIO_PURPLE)
        elif color.lower() == 'yellow':
            radio = self.wait_for_element_visible(self.RADIO_YELLOW)
        else:
            raise ValueError(f"Invalid radio button color: {color}")
        
        return radio.is_selected()
    
    def is_radio_button_disabled(self, vegetable):
        """
        Check if a radio button is disabled
        
        Args:
            vegetable: Vegetable of the radio button ('cabbage', 'pumpkin')
            
        Returns:
            bool: True if disabled, False otherwise
        """
        if vegetable.lower() == 'cabbage':
            radio = self.wait_for_element_visible(self.RADIO_CABBAGE)
        elif vegetable.lower() == 'pumpkin':
            radio = self.wait_for_element_visible(self.RADIO_PUMPKIN)
        else:
            raise ValueError(f"Invalid vegetable: {vegetable}")
        
        return not radio.is_enabled() 