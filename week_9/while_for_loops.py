#WHILE LOOPS

# while loop = execute some code WHILE some condition remains true
# while loops and for loops
# are fotms of iteration
# repeating ot looping through
# a set of steps or instructions
# to iterate is the verb
# form of iteration
# be careful of infinite loops
# they will crash your program
# and you will have to restart it
# infinite loops are loops that never end

# name = input("Enter your name")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}")

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit) : ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

#FOR LOOPS

# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, strings, sequence, etc.

# for x in reversed (range(1, 11, 3)): 
#     print(x)

# print("HAPPY NEW YEAR!!!!!!!!!!!!!")

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         break# continue #skip something
#     else:
#         print(x)
#Challenge 3
horror_movies = ['The Exorcist', 'The Shining', 'The Conjuring', 'The Ring']
for x in horror_movies:
    if x == 'The Shining':
        print("The Shining")
        break
    else:
        print("The Shining was not found.")
        print(x)
#Challenge 2
horror_characters = []
user_input = input("Enter a horror movie character (Press q to quit): ")
while not user_input == "q":
    horror_characters.append(user_input)
    user_input = input("Enter a horror movie character (Press q to quit): ")
    

print(horror_characters)

for character in horror_characters:
    if character == "Ghostface":
        continue
    print(character)

#Challenge 3
horror_characters = []
user_input = input("Enter a horror movie character (Press q to quit): ")

while user_input != 'q':
    horror_characters.append(user_input)
    user_input = input("enter a horror movie character (Press q to quit): ")
for char in range(len(horror_characters)):
    if horror_characters[char] == "Pennywise":
        horror_characters[char] = "[REDACTED]"
print(horror_characters)