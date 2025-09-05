cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'

if requested_topping != 'anchioves':
    print('Hold the anchioves!')


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding Mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding Pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding Extra Cheese')
print('\n Finished making your pizza.')



if 'mushrooms' in requested_toppings:
    print('Adding Mushrooms')
elif'pepperoni' in requested_toppings:
    print('Adding Pepperoni')
elif 'extra cheese' in requested_toppings:  #elif isn't executed because if/elif/else stops the moment any object is true in list
    print('Adding Extra Cheese')
print('\n Finished making your pizza.')


requested_toppings2 = ['mushrooms', 'green peppers', 'cheese']

for requested_top in requested_toppings2:
    print(f"Adding Requested Topping {requested_top}")
print('\nFinished making pizza.')


for requested_top in requested_toppings2:
    if requested_top == 'green peppers':
        print('Sorry, we ran out of green peppers.')
    else:
        print(f"Adding Requested Topping {requested_top}") 
print('\nFinished making pizza.')


requested_toppings3 = []

if requested_toppings3:
    for requested_t in requested_toppings3:
        print(f"Adding {requested_t}")
    print("Finished making your pizza my dearest customer.")
else: 
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings4 = ['mushrooms', 'french fries', 'extra cheese']

print("\nHello! Welcome to Pizza World4!")
for r_t4 in requested_toppings4: 
    if r_t4 in available_toppings:
        print(f'Adding {r_t4}')
    else:
        print(f"Sorry, we don't have {r_t4} as an available topping.")

print(f'We finished making your pizza.')

