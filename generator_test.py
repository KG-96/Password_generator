"""Password generator and database tests using pytest"""
import main


def test_easy_password_lenght():
    """Test is checking lenght of generated password"""
    x = main.random.randint(5 , 20)
    assert x == len(main.easy_pass(x))

def test_UPCASES_easy_generator():
    """Test is checking that password have uppercase sings"""
    counter = 0
    lenght = main.random.randint(5, 20)
    password = main.easy_pass(lenght)
    for x in main.UPPERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_LOWERCASES_easy_generator():
    """Test is checking that password have lowercase sings"""
    counter = 0
    lenght = main.random.randint(5, 20)
    password = main.easy_pass(lenght)
    for x in main.LOWERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_easy_generator():
    """Test is checking that password is without digit signs"""
    counter = 0
    lenght = main.random.randint(5, 20)
    password = main.easy_pass(lenght)
    for x in main.DIGITS:
        if x in password:
            counter += 1
    assert counter == 0

def test_SPECIAL_SIGNS_easy_generator():
    """Test is checking that password is without special sings"""
    counter = 0
    a = main.random.randint(5, 20)
    lenght = main.random.randint(5, 20)
    password = main.easy_pass(lenght)
    for x in main.SPECIAL:
        if x in password:
            counter += 1
    assert counter == 0

def test_medium_password_lenght():
    """Test is checking lenght of generated password"""
    x = main.random.randint(8, 20)
    assert x == len(main.medium_pass(x))

def test_UPCASES_medium_generator():
    """Test is checking that password have uppercase sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.medium_pass(lenght)
    for x in main.UPPERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_LOWERCASES_medium_generator():
    """Test is checking that password have lowercase sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.medium_pass(lenght)
    for x in main.LOWERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_medium_generator():
    """Test is checking that password have digit sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.medium_pass(lenght)
    for x in main.DIGITS:
        if x in password:
            counter += 1
    assert counter > 0

def test_SPECIAL_SIGNS_medium_generator():
    """Test is checking that password is without special sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.medium_pass(lenght)
    for x in main.SPECIAL:
        if x in password:
            counter += 1
    assert counter == 0
    
    
def test_strong_password_lenght():
    """Test is checking lenght of generated password"""
    x = main.random.randint(8 , 20)
    assert x == len(main.strong_pass(x))

def test_UPCASES_strong_generator():
    """Test is checking that password have uppercase sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.strong_pass(lenght)
    for x in main.UPPERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_LOWERCASES_strong_generator():
    """Test is checking that password have lowercase sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.strong_pass(lenght)
    for x in main.LOWERCASE:
        if x in password:
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_strong_generator():
    """Test is checking that password have digit sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.strong_pass(lenght)
    for x in main.DIGITS:
        if x in password:
            counter += 1
    assert counter > 0

def test_SPECIAL_SIGNS_strong_generator():
    """Test is checking that password have special sings"""
    counter = 0
    lenght = main.random.randint(8, 20)
    password = main.strong_pass(lenght)
    for x in main.SPECIAL:
        if x in password:
            counter += 1
    assert counter > 0


def test_DATABASE_last_ADDED():
    """Test is chcecking connection with database and last add object"""
    a = main.random.randint(5, 20)
    password = main.strong_pass(a)
    collection = main.database.get_db()
    assert password == collection[-1]['password']


