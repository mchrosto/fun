###Chapter 4#####

family_members = ['matt', 'andrea', 'halina', 'manan', 'meera', 'arya']
for member in family_members:
    print(member)


for member in family_members:
    print(f"{member.title()}, that was a great t[rick!")


pizzas = ['Cheese', 'Pepperoni', 'Hawaiian']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print(f"I love pizza.")


for value in range(1, 6):
    print(value)


numbers = list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 20, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)    

squares2 = [value**2 for value in range(1,11)]
print(squares2)
#indent difference between line 34


players = ['charles', 'martina', 'michael', 'florece', 'eli']
print(players[0:3])

for player in players[0:4]:
    print(player)
    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

dimensions = (200, 5)
#print(dimensions[0])
#print(dimensions[1]) proves tuples are real

for dimension in dimensions:
    print(dimension)

print("Original Dimension")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimenisons:")
for dimension in dimensions: 
    print(dimension)


######Chapter 5###########


