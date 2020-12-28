def greet_user():
    """Display a simple greeting."""
    print("Hello")
greet_user()


def greet_user(name):
    """Display a simple greeting."""
    print(f"Hello {name.title()}")
greet_user('jesse')


def describe_pet(animal_type, pet_name):
    """Display information about the pat"""
    print(f"I have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='dog', pet_name='harry')
describe_pet(pet_name='harry', animal_type='dog')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about the pat"""
    print(f"I have {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('harry')
describe_pet(pet_name='harry', animal_type='cat')


def square(num):
    """Squares the number"""
    return num**2

num_squared = square(5)
print(num_squared)


def format_name(first_name, last_name, middle_name=''):
    """Prints formatted name"""
    if middle_name:
        print(f"{first_name} {middle_name} {last_name}")
    else:
        print(f"{first_name} {last_name}")

format_name('Vladimir', 'Rajevac', 'Mogi')
format_name('Vladimir', 'Rajevac')


def multiple(num1, num2, num3=None):
    """Multiple numbers"""
    if num3:
        return num1 * num2 * num3
    else:
        return num1 * num2

print(multiple(2, 3))


def build_person(first_name, last_name):
    """Returns dictionary with person name"""
    person = {"first": {first_name}, "last": {last_name}}
    return person

person_name = build_person("Vladimir", "Rajevac")
print(person_name['first'])


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)


def get_user_names(names):
    """Print user names"""
    for name in names:
        print(name)
user_names = ['Vladimir', 'Wen', 'Cilka']
get_user_names(user_names)


