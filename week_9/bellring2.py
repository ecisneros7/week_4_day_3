#Question 1: Movie Ticket Price
print("This is Movie Ticket Price Question")
#Ask the user for their input
age = int(input("How old are you? "))
#Ask the user if they have a membership
memStatus = input("Y or N, do you have a membership with us? ")
#Now this checks to see if the user is under 18 or not
if age < 18:
    print("Youth ticket price is $10.") #If they are under 18, they get the youth ticket price which is $10
elif 18 <= age < 65: #This is the range where the user qualifies as an adult
    if memStatus == 'Y': #If the adult has a membership,
        print("Discount adult ticket price is $12") #They get the discounted price: #12
    else:
        print("Regular adult ticket price is $15.") #If they don't have a membership, they get the regular price: $15
elif age >= 65: #now this checks if the user is a Senior; this is the range that makes them a Senior
    print("Senior ticket price is $8.") #If they are a Senior, they get the Senior ticket price of $8

#Question 5: Tech Support Troubleshoot
print("This is Tech Support Troubleshoot Question") #this is just a thing that helps the terminal look more organized
computerOn = input("Y or N, is your computer on? ") #This asks the user if they have their computer on and we ask for Y or N to avoid the user using any other responses as it'll lead to an error
wifi = input("Y or N, is your computer connected to the Wi-Fi? ") #we do the same here to ask if their Wi-Fi is turned on and connected to their computer.
if computerOn == 'Y': #if the computer is on, 
    if wifi == 'Y': #it'll check if the computer is connected to the Wi-Fi
            print("You're in!") #If they are, this prints out.
    elif wifi == 'N': #if they aren't connected, 
            icon = input("Y or N, does your computer display the Wi-Fi icon? ") #this input will be shown to ask the user to check if their computer displays a Wi-Fi icon.
            if icon == 'Y': #If it does display that,
                print("Try reconnecting to the Wi-Fi network!") #this prints out, 
            if icon == 'N': #and if it isn't shown,
                print("Please check your Wi-Fi settings or contact support!") #then this is displayed
elif computerOn == 'N': #reversing back to the 'Is your computer on?' question, if it's not on, it stop any further checking and questions and-
        print("Turn on your computer.") #- prints this out saying to turn on the computer before proceeding any further.