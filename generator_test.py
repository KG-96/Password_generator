import main


def test_easy_password_lenght():
    x = main.random.randint(5 , 20)
    assert x == len(main.easy_pass(x))

def test_UPCASES_easy_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.UPPERCASE:
        if x in main.easy_pass(a):
            counter += 1
    assert counter > 0


def test_LOWERCASES_easy_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.LOWERCASE:
        if x in main.easy_pass(a):
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_easy_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.DIGITS:
        if x in main.easy_pass(a):
            counter += 1
    assert counter == 0

def test_SPECIAL_SIGNS_easy_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.SPECIAL:
        if x in main.easy_pass(a):
            counter += 1
    assert counter == 0

def test_medium_password_lenght():
    x = main.random.randint(5 , 20)
    assert x == len(main.medium_pass(x))

def test_UPCASES_medium_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.UPPERCASE:
        if x in main.medium_pass(a):
            counter += 1
    assert counter > 0


def test_LOWERCASES_medium_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.LOWERCASE:
        if x in main.medium_pass(a):
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_medium_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.DIGITS:
        if x in main.medium_pass(a):
            counter += 1
    assert counter > 0

def test_SPECIAL_SIGNS_medium_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.SPECIAL:
        if x in main.medium_pass(a):
            counter += 1
    assert counter == 0
    
    
def test_strong_password_lenght():
    x = main.random.randint(5 , 20)
    assert x == len(main.strong_pass(x))

def test_UPCASES_strong_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.UPPERCASE:
        if x in main.strong_pass(a):
            counter += 1
    assert counter > 0


def test_LOWERCASES_strong_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.LOWERCASE:
        if x in main.strong_pass(a):
            counter += 1
    assert counter > 0


def test_DIGIT_SIGNS_strong_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.DIGITS:
        if x in main.strong_pass(a):
            counter += 1
    assert counter > 0

def test_SPECIAL_SIGNS_strong_generator():
    counter = 0
    a = main.random.randint(5, 20)
    for x in main.SPECIAL:
        if x in main.strong_pass(a):
            counter += 1
    assert counter > 0


def test_DATABASE_last_ADDED():
    a = main.random.randint(5, 20)
    password = main.strong_pass(a)
    collection = main.database.get_db()
    assert password == collection[-1]['password']


