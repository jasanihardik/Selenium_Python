from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class TodoListPage(BasePage):
    """Page object for WebDriverUniversity Todo List page"""
    
    # Locators
    TODO_ITEMS = (By.CSS_SELECTOR, "ul li")
    ADD_NEW_TODO_INPUT = (By.XPATH, "//input[@placeholder='Add new todo']")
    TODO_ITEM_TEXT = lambda self, item_text: (By.XPATH, f"//li[contains(text(), '{item_text}')]")
    TODO_ITEM_DELETE = lambda self, item_text: (By.XPATH, f"//li[contains(text(), '{item_text}')]/span/i")
    HIDDEN_TODOS = (By.CSS_SELECTOR, "ul li.completed")
    
    def __init__(self, driver):
        """Initialize the TodoListPage object"""
        super().__init__(driver)
    
    def get_todo_items(self):
        """
        Get all todo items
        
        Returns:
            list: List of todo items
        """
        self.logger.info("Getting all todo items")
        # Allow some time for the page to fully load
        time.sleep(1)
        elements = self.wait_for_elements_visible(self.TODO_ITEMS)
        return [element.text for element in elements]
    
    def add_todo_item(self, text):
        """
        Add a new todo item
        
        Args:
            text: Text of the todo item
            
        Returns:
            TodoListPage: Self reference for method chaining
        """
        self.logger.info(f"Adding todo item: {text}")
        input_field = self.wait_for_element_visible(self.ADD_NEW_TODO_INPUT)
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(Keys.RETURN)
        # Allow some time for the item to be added
        time.sleep(1)
        return self
    
    def mark_todo_as_complete(self, item_text):
        """
        Mark a todo item as complete
        
        Args:
            item_text: Text of the todo item
            
        Returns:
            TodoListPage: Self reference for method chaining
        """
        self.logger.info(f"Marking todo item as complete: {item_text}")
        item = self.wait_for_element_clickable(self.TODO_ITEM_TEXT(item_text))
        item.click()
        # Allow some time for the state to change
        time.sleep(1)
        return self
    
    def delete_todo_item(self, item_text):
        """
        Delete a todo item
        
        Args:
            item_text: Text of the todo item
            
        Returns:
            TodoListPage: Self reference for method chaining
        """
        self.logger.info(f"Deleting todo item: {item_text}")
        # First hover over the item to make the delete button visible
        item = self.wait_for_element_visible(self.TODO_ITEM_TEXT(item_text))
        
        try:
            # Try to use JavaScript to delete the item if hover doesn't work
            delete_button_xpath = f"//li[contains(text(), '{item_text}')]/span/i"
            delete_button = self.driver.find_element(By.XPATH, delete_button_xpath)
            self.driver.execute_script("arguments[0].click();", delete_button)
        except:
            # Fallback to hover and click
            self.hover(self.TODO_ITEM_TEXT(item_text))
            delete_button = self.wait_for_element_clickable(self.TODO_ITEM_DELETE(item_text))
            delete_button.click()
        
        # Allow some time for the item to be deleted
        time.sleep(1)
        return self
    
    def is_todo_item_present(self, item_text):
        """
        Check if a todo item is present
        
        Args:
            item_text: Text of the todo item
            
        Returns:
            bool: True if the item is present, False otherwise
        """
        self.logger.info(f"Checking if todo item is present: {item_text}")
        # Allow some time for the page to update
        time.sleep(1)
        try:
            elements = self.driver.find_elements(By.XPATH, f"//li[contains(text(), '{item_text}')]")
            return len(elements) > 0
        except:
            return False
    
    def is_todo_item_completed(self, item_text):
        """
        Check if a todo item is marked as completed
        
        Args:
            item_text: Text of the todo item
            
        Returns:
            bool: True if the item is completed, False otherwise
        """
        self.logger.info(f"Checking if todo item is completed: {item_text}")
        try:
            item = self.wait_for_element_visible(self.TODO_ITEM_TEXT(item_text))
            return "completed" in item.get_attribute("class")
        except:
            return False
    
    def get_completed_items_count(self):
        """
        Get the count of completed items
        
        Returns:
            int: Number of completed items
        """
        self.logger.info("Getting count of completed items")
        try:
            elements = self.driver.find_elements(*self.HIDDEN_TODOS)
            return len(elements)
        except:
            return 0 