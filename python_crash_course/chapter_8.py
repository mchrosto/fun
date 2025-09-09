def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()



def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")
greet_user('jesse')


def display_message():
    """Tells everyone a message"""
    print(f"Hello! I am learning about functions!")

display_message()

def favorite_book():
    books = ['Slaughterhouse-Five', 'One Hundred Years of Solitude']
    for book in books:
        print(f"My favorite book is {book}!")

favorite_book()

def describe_pet(animal_type, pet_name):
    """Display pet name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('Dog', 'Rufus')
describe_pet('Cat', 'Molly')


describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


def describe_pet(pet_name,animal_type='dog'):
    """Display pet name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='willie')

def get_formatted_name(first_name, last_name):
    """Return a formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)

def get_formatted_person(first_name, middle_name, last_name):
    person = f"{first_name} {middle_name} {last_name}"
    return person

musician = get_formatted_person('Andrea', 'Lynn', 'Schiliro')
print(musician)



def get_formatted_person(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_person('Andrea', 'Lynn', 'Schiliro')
musician2 = get_formatted_person('Matt', 'Chrostowski')
print(musician)
print(musician2)

