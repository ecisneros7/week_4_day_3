# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
string="abracadabra"
print(string[4])
print(string[-2])
print(string.find("c"))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
abc="abcdefghijklmnopqrstuvwxyz"
print(abc[7:10])
print(abc[0:14:2])
print(abc[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
# Manipulating Words: 
extract="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
name=(extract[83:-1])

# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
words = info.split()
# b. Extract every third word.
every_third_word=words[::3]
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
result= ' '.join(every_third_word)
print(result)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
shout="MAY THE FORCE BE WITH YOU"
calmDown=(shout.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto=["make", "haste", "slowly"]
joined=" ".join(motto)
print(joined)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
quote="Life is what happens when you are busy making other plans."
print(quote.replace("busy", "distracted"))
print(quote.replace("plans", "mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
result = "iteration " 
repeatingandrepeating=result* 7
print(repeatingandrepeating)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
moonlight="moonlight"
check=moonlight in text
print(check)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
long="Supercalifragilisticexpialidocious"
howmuch=len(long)
print(howmuch)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
