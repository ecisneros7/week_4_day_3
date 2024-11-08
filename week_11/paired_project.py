#Problem 1
score = 0
#these values below determine the count or amount of scores that become categorized
excellent = 0
good = 0
pass_count = 0
fail = 0
while score >= 0: #this here is keep the while loop running, whatever positive numbr is inputted, the loop will repeat forever
    score = int(input("Please enter a score: ")) #the user inputs a number, for example, we'll use 84
    if score >= 90: #now for scores greater than or equal to 90. it'll be classified as 'Excellent'
        print("Excellent") #now the system will declare it's category if conditions are met
        excellent = excellent + 1 #Once the number is indeed within these conditions, it'll be classified as 'Excellent' and the amount of 'Excellent' scores goes up by one. Here, our number 84 doesn't fit this category.
    elif 70<= score <= 89: #this category is meant for scores between 70-89. Our number 84 fits these conditions.
        print("Good") #the system will declare this number/score of ours to be 'Good'.
        good = good + 1 #conditions were met so the amount of Good scores will increase by one.
    elif 50<= score <= 69: #for a passing grade, the number needs to be at least 50 but less than 69
        print("Pass") #system will declare it's a passing grade if conditions are met
        pass_count = pass_count + 1 #amount of passing grades will increase
    elif 0 <= score < 50: #a failing grade is classified as less than 50, but we'll add in at least greater than or equal to 0 so a negative number doesn't count as a failing grade but instead an invalid input
        print("Fail") #the system will declare it is a failing grade
        fail = fail + 1 #the amount of failing grades will increase by one
    else:
        print("Error: Can not be negative number.") #now if the user puts a negative number, the eternal loop ends. It states that a negative number is invalid.
        print("Let's proceed to the counts of each score you inputted.") #It now prepares to declare the amount of scores that fit each category's conditions.
        break #this is the real measure that prevents the looping from functioning again, effectivley ending it
print(f"The amount of excellent scores are {excellent}") #prints the amount of scores that were excellent
print(f"The amount of good scores are {good}") #prints the amount of scores that were good
print(f"The amount of passing scores are {pass_count}") #prints the amount of scores that were passing
print(f"The amount of failing scores are {fail}") #prints the amount of scores that were failing

#Problem 2
starting = int(input("Please type what number you'd like to have as the starting number: ")) #asks the user for the first number to determine the range
ending = int(input("Please type what number you'd like to have as the ending number: ")) #asks the user for the last number to determine the range
special_even = 0 #this is the amount of numbers that met this condition, now 0
special_odd = 0 #this is the amount of numbers that met this condition, now 0
for number in range(starting, ending): #a range is now made using the numbers the user inputted
    if number%2 == 0: #checks if the number is even
        if number > 10: #the part that determines if the number is a 'special' even
            special_even = special_even + 1 #if it was greater than 10, it met the condition and is classified as a special even and the count goes up by one
    if number%2 != 0: #checks if the number is odd
        if number < 20: #the part that determines if the number classifies as a 'special' odd
            special_odd = special_odd + 1 #if the number was odd AND less than 20, it qualifies as a special odd and the amount of special odds goes up by one
# any even or odd numbers that didn't meet the second condition was not classified in either category and excluded from any count
total_range = ending - starting #counts the total numbers within the range for comparision
print(f"Out of all the {total_range} numbers you had,") #declares amount of numbers checked in the range
print(f"The amount of numbers that classified as special evens within your range was: {special_even}") #the amount of special evens
print(f"The amount of numbers that classified as special odds within your range was: {special_odd}") #the amount of special odds