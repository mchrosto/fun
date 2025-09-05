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

