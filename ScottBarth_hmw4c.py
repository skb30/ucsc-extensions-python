# Count my change


import random

# calcuate function
def countChange(quaters, dimes, nickels, pennies):
    return ((quaters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100.00


# unit tests
# print countChange(0, 0, 0, 0)  # result should be .25
# print countChange(1, 0, 0, 0)  # result should be .25
# print countChange(0, 1, 0, 0)  # result should be .10
# print countChange(0, 0, 1, 0)  # result should be .05
# print countChange(0, 0, 0, 1)  # result should be .01
# print countChange(4, 8, 1, 1)  # result should be 1.86

# get the user's name or ask to quit
name  = raw_input("Please enter you name or [Enter/Return] to quit> ")

if name == '':
    print "Good Bye. "
    exit()
else:
    quaters = int(raw_input("Please enter the number of quaters> "))
    dimes   = int(raw_input("Please enter the number of dimes> "))
    nickels = int(raw_input("Please enter the number of nickels> "))
    pennies = int(raw_input("Please enter the number of pennies> "))


# call the function and print the report
print "All Counted, " + name + " has $" + str(countChange(quaters, dimes, nickels, pennies))

# create a random message
ran = random.randint(1,3)

if ran == 1:
    print"Wow, that's a lot of money!"
elif ran == 2:
    print"Need to save more."
else:
    print "Time to put cash in the bank"