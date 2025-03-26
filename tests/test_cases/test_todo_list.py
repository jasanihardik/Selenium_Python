import pytest
from pages.home_page import HomePage
from utilities.logger import setup_logger

# Set up logger for this test module
logger = setup_logger("TodoListTests")

class TestTodoList:
    """Test the Todo List functionality"""
    
    def test_add_todo_item(self, driver):
        """Test that a new todo item can be added"""
        logger.info("Starting test_add_todo_item")
        
        # Navigate to homepage and then to Todo List page
        home_page = HomePage(driver)
        home_page.open()
        todo_page = home_page.click_to_do_list()
        
        # Add a new todo item
        new_todo = "Test automation with Selenium"
        todo_page.add_todo_item(new_todo)
        
        # Verify the item was added
        todo_items = todo_page.get_todo_items()
        assert new_todo in todo_items, f"Todo item '{new_todo}' was not found in the list"
        
        logger.info("test_add_todo_item completed successfully")
    
    def test_mark_todo_as_complete(self, driver):
        """Test that a todo item can be marked as complete"""
        logger.info("Starting test_mark_todo_as_complete")
        
        # Navigate to homepage and then to Todo List page
        home_page = HomePage(driver)
        home_page.open()
        todo_page = home_page.click_to_do_list()
        
        # Add a new todo item
        new_todo = "Mark this task as complete"
        todo_page.add_todo_item(new_todo)
        
        # Mark the item as complete
        todo_page.mark_todo_as_complete(new_todo)
        
        # Verify the item is marked as complete
        assert todo_page.is_todo_item_completed(new_todo), f"Todo item '{new_todo}' was not marked as complete"
        
        logger.info("test_mark_todo_as_complete completed successfully")
    
    def test_delete_todo_item(self, driver):
        """Test that a todo item can be deleted"""
        logger.info("Starting test_delete_todo_item")
        
        # Navigate to homepage and then to Todo List page
        home_page = HomePage(driver)
        home_page.open()
        todo_page = home_page.click_to_do_list()
        
        # Add a new todo item
        new_todo = "Delete this task"
        todo_page.add_todo_item(new_todo)
        
        # Verify the item was added
        assert todo_page.is_todo_item_present(new_todo), f"Todo item '{new_todo}' was not found in the list"
        
        # Delete the item
        todo_page.delete_todo_item(new_todo)
        
        # Verify the item was deleted
        assert not todo_page.is_todo_item_present(new_todo), f"Todo item '{new_todo}' was not deleted"
        
        logger.info("test_delete_todo_item completed successfully")
    
    def test_multiple_todo_items(self, driver):
        """Test adding, completing, and deleting multiple todo items"""
        logger.info("Starting test_multiple_todo_items")
        
        # Navigate to homepage and then to Todo List page
        home_page = HomePage(driver)
        home_page.open()
        todo_page = home_page.click_to_do_list()
        
        # Add multiple todo items
        todos = ["First task", "Second task", "Third task"]
        for todo in todos:
            todo_page.add_todo_item(todo)
        
        # Verify all items were added
        todo_items = todo_page.get_todo_items()
        for todo in todos:
            assert todo in todo_items, f"Todo item '{todo}' was not found in the list"
        
        # Mark some items as complete
        todo_page.mark_todo_as_complete(todos[0])
        todo_page.mark_todo_as_complete(todos[2])
        
        # Verify the items are marked as complete
        assert todo_page.is_todo_item_completed(todos[0]), f"Todo item '{todos[0]}' was not marked as complete"
        assert todo_page.is_todo_item_completed(todos[2]), f"Todo item '{todos[2]}' was not marked as complete"
        assert not todo_page.is_todo_item_completed(todos[1]), f"Todo item '{todos[1]}' should not be marked as complete"
        
        # Delete one item
        todo_page.delete_todo_item(todos[1])
        
        # Verify the item was deleted
        assert not todo_page.is_todo_item_present(todos[1]), f"Todo item '{todos[1]}' was not deleted"
        assert todo_page.is_todo_item_present(todos[0]), f"Todo item '{todos[0]}' should still be present"
        assert todo_page.is_todo_item_present(todos[2]), f"Todo item '{todos[2]}' should still be present"
        
        logger.info("test_multiple_todo_items completed successfully") 