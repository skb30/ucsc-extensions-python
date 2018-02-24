# Homework 5 - Lists (Math with Lists)

### Create a program that does some simple math on a list of numbers.

numberList = []
# prompt user to start the game
while True:
    num = raw_input("Please enter a number or [Return/Enter] to quit> ")
    if num == "" :
        break

    numberList.append(float(num))

if len(numberList) == 0:
    print "You must enter a number to play the game. "
    exit(0)

smallest = numberList[0]
largest = numberList[0]
sum = 0

# print the list of numbers
for i in(numberList):
    print i

# determine the smallest number in the list
for number in numberList:
    if number < smallest:
        smaller = number

# determine the largest number in the list
for number in numberList:
    if number > largest:
        largest = number

# sum the numbers in the list
for number in numberList:
    sum += number

# calculate the average
average = sum / len(numberList)

# print the reports
print "The smallest number in the list is: " + str(smaller)
print "The largest number in the list is: " + str(largest)
print "The sum of the numbers in the list is: " + str(sum)
print "The average of the numbers in the list is: " + str(average)






