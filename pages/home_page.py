from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL

class HomePage(BasePage):
    """Page object for the WebDriverUniversity homepage"""
    
    # URL
    URL = BASE_URL
    
    # Locators
    CONTACT_US_LINK = (By.CSS_SELECTOR, "#contact-us")
    LOGIN_PORTAL_LINK = (By.CSS_SELECTOR, "#login-portal")
    BUTTON_CLICKS_LINK = (By.CSS_SELECTOR, "#button-clicks")
    TO_DO_LIST_LINK = (By.CSS_SELECTOR, "#to-do-list")
    PAGE_OBJECT_MODEL_LINK = (By.CSS_SELECTOR, "#page-object-model")
    ACCORDION_LINK = (By.CSS_SELECTOR, "#accordion")
    DROPDOWN_LINK = (By.CSS_SELECTOR, "#dropdown-checkboxes-radiobuttons")
    AJAX_LOADER_LINK = (By.CSS_SELECTOR, "#ajax-loader")
    ACTIONS_LINK = (By.CSS_SELECTOR, "#actions")
    SCROLLING_LINK = (By.CSS_SELECTOR, "#scrolling-around")
    POPUP_ALERTS_LINK = (By.CSS_SELECTOR, "#popup-alerts")
    IFRAME_LINK = (By.CSS_SELECTOR, "#iframe")
    HIDDEN_ELEMENTS_LINK = (By.CSS_SELECTOR, "#hidden-elements")
    DATA_TABLE_LINK = (By.CSS_SELECTOR, "#data-table")
    FILE_UPLOAD_LINK = (By.CSS_SELECTOR, "#file-upload")
    DATEPICKER_LINK = (By.CSS_SELECTOR, "#datepicker")
    
    def __init__(self, driver):
        """Initialize the HomePage object"""
        super().__init__(driver)
    
    def open(self):
        """Open the homepage"""
        self.navigate_to(self.URL)
        return self
    
    def click_contact_us(self):
        """
        Click on the Contact Us link
        
        Returns:
            ContactUsPage: The Contact Us page
        """
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.CONTACT_US_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.contact_us_page import ContactUsPage
        return ContactUsPage(self.driver)
    
    def click_login_portal(self):
        """Click on the Login Portal link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.LOGIN_PORTAL_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
                
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    def click_button_clicks(self):
        """Click on the Button Clicks link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.BUTTON_CLICKS_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.button_clicks_page import ButtonClicksPage
        return ButtonClicksPage(self.driver)
    
    def click_to_do_list(self):
        """Click on the To Do List link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.TO_DO_LIST_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.todo_list_page import TodoListPage
        return TodoListPage(self.driver)
    
    def click_dropdown_checkboxes_radiobuttons(self):
        """Click on the Dropdown, Checkboxes, Radiobuttons link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.DROPDOWN_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.dropdown_page import DropdownPage
        return DropdownPage(self.driver)
    
    def click_actions(self):
        """Click on the Actions link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.ACTIONS_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.actions_page import ActionsPage
        return ActionsPage(self.driver)
    
    def click_popup_alerts(self):
        """Click on the Popup & Alerts link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.POPUP_ALERTS_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.popup_alerts_page import PopupAlertsPage
        return PopupAlertsPage(self.driver)
    
    def click_ajax_loader(self):
        """Click on the Ajax Loader link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.AJAX_LOADER_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.ajax_loader_page import AjaxLoaderPage
        return AjaxLoaderPage(self.driver)
    
    def click_accordion(self):
        """Click on the Accordion link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.ACCORDION_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.accordion_page import AccordionPage
        return AccordionPage(self.driver)
    
    def click_file_upload(self):
        """Click on the File Upload link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.FILE_UPLOAD_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.file_upload_page import FileUploadPage
        return FileUploadPage(self.driver)
    
    def click_datepicker(self):
        """Click on the Datepicker link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.DATEPICKER_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.datepicker_page import DatepickerPage
        return DatepickerPage(self.driver)
    
    def click_iframe(self):
        """Click on the IFrame link"""
        # Store the original window handle
        original_window = self.driver.current_window_handle
        
        # Close any other windows except the original one
        if len(self.driver.window_handles) > 1:
            for handle in self.driver.window_handles:
                if handle != original_window:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
            self.driver.switch_to.window(original_window)
        
        # Click the link
        self.click(self.IFRAME_LINK)
        
        # Switch to the new window
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        
        from pages.iframe_page import IframePage
        return IframePage(self.driver)
    
    def get_all_links(self):
        """Get all links on the homepage"""
        links = {
            'contact_us': self.is_element_displayed(self.CONTACT_US_LINK),
            'login_portal': self.is_element_displayed(self.LOGIN_PORTAL_LINK),
            'button_clicks': self.is_element_displayed(self.BUTTON_CLICKS_LINK),
            'to_do_list': self.is_element_displayed(self.TO_DO_LIST_LINK),
            'page_object_model': self.is_element_displayed(self.PAGE_OBJECT_MODEL_LINK),
            'accordion': self.is_element_displayed(self.ACCORDION_LINK),
            'dropdown': self.is_element_displayed(self.DROPDOWN_LINK),
            'ajax_loader': self.is_element_displayed(self.AJAX_LOADER_LINK),
            'actions': self.is_element_displayed(self.ACTIONS_LINK),
            'scrolling': self.is_element_displayed(self.SCROLLING_LINK),
            'popup_alerts': self.is_element_displayed(self.POPUP_ALERTS_LINK),
            'iframe': self.is_element_displayed(self.IFRAME_LINK),
            'hidden_elements': self.is_element_displayed(self.HIDDEN_ELEMENTS_LINK),
            'data_table': self.is_element_displayed(self.DATA_TABLE_LINK),
            'file_upload': self.is_element_displayed(self.FILE_UPLOAD_LINK),
            'datepicker': self.is_element_displayed(self.DATEPICKER_LINK)
        }
        return links 