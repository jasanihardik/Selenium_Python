import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("DropdownTests")

class TestDropdown:
    """Test the Dropdown, Checkboxes, and Radiobuttons functionality"""
    
    def test_select_dropdown_values(self, driver):
        """Test that a user can select values from dropdown menus"""
        logger.info("Starting test_select_dropdown_values")
        
        # Navigate to homepage and then to Dropdown page
        home_page = HomePage(driver)
        home_page.open()
        dropdown_page = home_page.click_dropdown_checkboxes_radiobuttons()
        
        # Select values from dropdowns
        dropdown_page.select_dropdown_value(1, "Python")
        dropdown_page.select_dropdown_value(2, "Maven")
        dropdown_page.select_dropdown_value(3, "JavaScript")
        
        # Verify the selected values
        assert dropdown_page.get_dropdown_selected_value(1) == "Python", "First dropdown value not set correctly"
        assert dropdown_page.get_dropdown_selected_value(2) == "Maven", "Second dropdown value not set correctly"
        assert dropdown_page.get_dropdown_selected_value(3) == "JavaScript", "Third dropdown value not set correctly"
        
        logger.info("test_select_dropdown_values completed successfully")
    
    def test_checkbox_functionality(self, driver):
        """Test that a user can check and uncheck checkboxes"""
        logger.info("Starting test_checkbox_functionality")
        
        # Navigate to homepage and then to Dropdown page
        home_page = HomePage(driver)
        home_page.open()
        dropdown_page = home_page.click_dropdown_checkboxes_radiobuttons()
        
        # Check and uncheck checkboxes
        dropdown_page.check_checkbox(1)
        dropdown_page.check_checkbox(2)
        dropdown_page.uncheck_checkbox(3)  # Option 3 is checked by default
        dropdown_page.check_checkbox(4)
        
        # Verify the checkbox states
        assert dropdown_page.is_checkbox_checked(1), "Checkbox 1 should be checked"
        assert dropdown_page.is_checkbox_checked(2), "Checkbox 2 should be checked"
        assert not dropdown_page.is_checkbox_checked(3), "Checkbox 3 should be unchecked"
        assert dropdown_page.is_checkbox_checked(4), "Checkbox 4 should be checked"
        
        logger.info("test_checkbox_functionality completed successfully")
    
    def test_radio_button_selection(self, driver):
        """Test that a user can select radio buttons"""
        logger.info("Starting test_radio_button_selection")
        
        # Navigate to homepage and then to Dropdown page
        home_page = HomePage(driver)
        home_page.open()
        dropdown_page = home_page.click_dropdown_checkboxes_radiobuttons()
        
        # Select a radio button (blue instead of green)
        dropdown_page.select_radio_button("blue")
        
        # Verify the radio button is selected
        assert dropdown_page.is_radio_button_selected("blue"), "Blue radio button should be selected"
        assert not dropdown_page.is_radio_button_selected("yellow"), "Yellow radio button should not be selected"
        assert not dropdown_page.is_radio_button_selected("orange"), "Orange radio button should not be selected"
        assert not dropdown_page.is_radio_button_selected("purple"), "Purple radio button should not be selected"
        
        logger.info("test_radio_button_selection completed successfully")
    
    def test_disabled_elements(self, driver):
        """Test that some elements are disabled"""
        logger.info("Starting test_disabled_elements")
        
        # Navigate to homepage and then to Dropdown page
        home_page = HomePage(driver)
        home_page.open()
        dropdown_page = home_page.click_dropdown_checkboxes_radiobuttons()
        
        # Verify the disabled radio buttons
        assert dropdown_page.is_radio_button_disabled("cabbage"), "Cabbage radio button should be disabled"
        assert not dropdown_page.is_radio_button_disabled("pumpkin"), "Pumpkin radio button should be enabled"
        
        logger.info("test_disabled_elements completed successfully") 