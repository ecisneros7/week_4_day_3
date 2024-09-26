#collection = single "variable" used to store multiple values
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "strawberries", "blueberries", "mango"]

print(fruits[::2])
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
#gives you length of list
#help gives you help about documentation
#attributes for a list
#::2 gives every 2
#::-1 makes it backwards
for fruit in fruits:
    print(fruit)
#this iterates over list
#for every fruit in fruits
fruits[1]="apple"
#this replaces 0 with whatever value you want
for fruit in fruits:
    print(fruit)
#the new value will show twice
fruits.append("apple")
# it adds something to the end of the list
fruits.remove("banana")
fruits.insert(0, "apple")
fruits.sort()
#puts stuff in alpabetical order
fruits.reverse()
#reverse the values on how you first inserted them
print(fruits)
fruits.clear()
#clears everything
print(fruits.index("apple"))
#finds the index of the element