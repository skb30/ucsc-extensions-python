# Roll the dice game
import random
def roll():
    return random.randint(1, 6)

# Data section
doubleCnt = 0.0


# prompt user to start the game and find out how many times to roll the dice.
while True:
    start = raw_input("Welcome to roll the dice! How many rolls would like to take?. ")
    start = int(start)
    if start > 10000000:
        print "Sorry that's too many times. Please try something smaller."
    else:
        break

# start the loop
for  i in range(1, start+1):
    die1 = roll()
    die2 = roll()

    # if the dice are equal we have doubles. Produce the doubles report.
    if die1 == die2:
        doubleCnt += 1


print "After " + str(i) + " rolls, we got " + str(int(doubleCnt)) + " doubles, " + str(float(doubleCnt / i) * 100) + '%'
print "Good Bye!"


