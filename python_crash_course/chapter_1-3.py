print("Hello. It's a Python Interpreter.")

message = "Hello World"
print(message)

message_2 = "Hello Puthon Crash Course reader."
print(message_2)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())

message_3 = f"Hello {first_name} {last_name}."
print(message_3)

print("\tPython")
print("Languages: \nPython \nJavscript")


favorite_language = 'python '
favorite_langauge2 = favorite_language.rstrip()
print(favorite_language)
print(favorite_langauge2)


bicycles = ['trek', 'comfortable', 'typical']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[-1])

message_4 = f"My first bicyle was a {bicycles[0].title()}"
print(message_4)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive} is too expensive for me.")

cars = ['bmw', 'jeep', 'honda', 'toyota']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

