import random
def roll():
    return random.randint(1, 6)


die1      = 0
die2      = 1
doubleCnt = 0
rollCnt   = 0
go        = 'y'
gameCnt   = 1

raw_input("Welcome to roll the dice! Press Enter to begin.")

while go == 'y':
# for n in range(10):
    die1 = roll()
    die2 = roll()


    if die1 == die2:
        doubleCnt += 1
        print "Round # " + str(gameCnt) + " You rolled a " + str(die1) + " and a " + str(die2)
        print "Doubles!!!"
        print float(doubleCnt / rollCnt)
        print "That is time number " + str(doubleCnt) + " you rolled doubles. Your % of doubles is: " + str(float(doubleCnt / rollCnt))

    else:
        print "Round # " + str(gameCnt) + " You rolled a " + str(die1) + " and a " + str(die2)
        rollCnt += 1
    while True:
        go = raw_input("Return or Enter continue, q to exit.")
        if go == 'q':
            break
        elif go == "":
            go = 'y'
            break
    gameCnt += 1

print "Good Bye!"