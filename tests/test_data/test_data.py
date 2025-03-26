class ContactFormData:
    """Test data for the Contact Us form"""
    
    VALID_DATA = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "comment": "This is a test message for the contact form."
    }
    
    MISSING_EMAIL_DATA = {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "",
        "comment": "This is a test message without an email."
    }
    
    MISSING_FIRST_NAME_DATA = {
        "first_name": "",
        "last_name": "Johnson",
        "email": "test@example.com",
        "comment": "This is a test message without a first name."
    }
    
    INVALID_EMAIL_DATA = {
        "first_name": "Mike",
        "last_name": "Brown",
        "email": "invalid-email",
        "comment": "This is a test message with an invalid email."
    }


class LoginData:
    """Test data for the Login Portal"""
    
    VALID_CREDENTIALS = {
        "username": "webdriver",
        "password": "webdriver123"
    }
    
    INVALID_CREDENTIALS = {
        "username": "invalid_user",
        "password": "invalid_password"
    }
    
    EMPTY_CREDENTIALS = {
        "username": "",
        "password": ""
    }
    
    USERNAME_ONLY = {
        "username": "webdriver",
        "password": ""
    }
    
    PASSWORD_ONLY = {
        "username": "",
        "password": "webdriver123"
    } 