#Ask the user to print a piece of text
text = input("Please insert a segment of text. ")
# #Now we will ask the user to input different letters to be able to see how many times these letters come up.
letter1 = input("Please enter any letter. ")
letter2 = input("Please enter another letter. ")
letter3 = input("Please enter one more letter. ")
#Now we need to convert the letters into lowercase letter so they're case insensitive
lower1 = letter1.lower()
lower2 = letter2.lower()
lower3 = letter3.lower()

lowerText = text.lower()

amountof1 = lowerText.count(lower1)
amountof2 = lowerText.count(lower2)
amountof3 = lowerText.count(lower3)
print(f"The amount of times that the first letter appeared in the text was {amountof1}")
print(f"The amount of times that the second letter appeared in the text was {amountof2}")
print(f"The amount of times that the third letter appeared in the text was {amountof3}")
# Now that we're done, we will begin to figure out the length or the amount of words in the text. To do this, we need to convert the text into a list.
textSplit = text.split()
textList = list(textSplit)
textWordLength = len(textList) 
print(textWordLength)

#Now we will try to find the first and last letter of the text that is inputted by the user
firstLetter = text[0]
print(firstLetter)
lastLetter = text[-1]
print(lastLetter)

#Now we want to reverse the list version of the text using the comman that inverts elements.
backwardsList = textList[::-1]
print(backwardsList)
#Now we are going to join both lists, backwards and the original
joinedList = " ".join(textList)
joinedbackwardsList = " ".join(backwardsList)
print(joinedList)
print(joinedbackwardsList)
#Lastly, we want to be able to check if the word "python" is in the text. We can simply do this by asking the program by using booleans.
python = "python"
ispythoninText = python in text
print(f"The statement that the text you inputted has the word 'Python' is {ispythoninText}")