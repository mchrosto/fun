##dictionaries 

alien_0 = {}
print(f"alien_0 is empty!")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"Congratulations! You've earned {new_points} points!")

#adding key/pairs to dictionaries
alien_0['x_position'] = 0
alien_0['y_position'] = 25 
print(alien_0)

#modifying dicitionaries
alien_0 = {'color': 'green'}
print(alien_0['color'])
alien_0 = {'color': 'yellow'}
print(alien_0['color'])



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 


alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


print("help")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite langauge is {language}")

point_value = favorite_languages.get('matt', 'Matt is not in dicitonary')
print(point_value)


user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi' }

for key, value in user_0.items(): 
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#looping through the key is the default for for loops and dicitionaries 

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())



friends = ['phil', 'sarah']
for name in favorite_languages.keys(): 
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


print(f"The following languages have been mentioned: ")
for langauge in favorite_languages.values():
    print(language.title())

print(favorite_languages.values())


for langauge in set(favorite_languages.values()):
    print(langauge.title()) #set = distinct in SQL

##Nesting 

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)





aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[5]:
    print(alien)
print("...")
print(f" Total Number of aliens: {len(aliens)}")

for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        print(alien['color'])
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    print(alien)


green_count = 0
for alien in aliens:
    if alien.get('color') == 'green':
        green_count += 1
print(green_count)

yellow_count = 0 
for alien in aliens: 
    if alien.get('color') == 'yellow':
        yellow_count += 1
print(f"{yellow_count} yellow aliens")

# green_count = sum(alien['color'] == 'green' )
# print(f"There are {green_count} green aliens")

#list in a dictionary 

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward':['rust', 'go'],
'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

###### for loop testiing

print(f"Other version: favorite langauges are: ")
for language in favorite_languages.values():
    print(f"\t{langauge.title()}")




users = {
    'aeinstein': {
        'first':  'albert',
        'last': 'einstein',
        'location': 'princeton',
    },  
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"Location: {location.title()}")






