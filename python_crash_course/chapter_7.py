# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}")

# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello {name}!")

# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)


# height = input(f"How tall are you, in inches? ")
# height = int(height)

# if height >= 48: 
#     print(f"\n You're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else: 
#     print(f"\nThe number {number} is odd.")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "Tell me something, and I will repeat it back to you: "
# prompt += "\n Enter 'quit' to end the program."

# # message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

#     if message == 'quit':
#         print("Parrot game over.")


# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else: 
#         print(message)


# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
# #         print(f"I'd love to go to {city.title()}")

# current_number = 0
# while current_number < 10: 
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

 

#Start with users that need to be verified. 
# and an empty list to hold confirmed users.

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# #Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# #Display current users.
# print(f"\nThe following users have been confirmed.")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())



pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

polling_active = True

while polling_active: 
    #Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond (yes/ no)")
    if repeat.upper() == "NO":
        polling_active = False

print(f"\n---Poll Results---")
for name, response in responses.items():
    print(f" {name} would like to climb {response}")





