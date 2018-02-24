# build a progam that contains a list, and allows the user to move back and forth within the list, and "warp-around" both ends
# of the list.


import random

myList = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']

index = random.randrange(0, len(myList))
startOfList = 0
endOfList = len(myList) - 1


print "The current element is: " + myList[index]
while True:
    # collect user input
    goAgain = raw_input("Press p for previous, n for next, or anything else to quit> ")

    # check and see if the user wants to quit the game.
    if goAgain != 'p' and goAgain != 'n':
        break
    # what command did the user enter? either 'p' or 'n'
    if goAgain == 'p':
        # decrement the index if were not at the beginning of the list.
        if index == startOfList:
            index = endOfList # move to the end of the list
        else:
            index -= 1
    else:
        # bump the index if were not at the end of the list.
        if index == endOfList:
            index = startOfList # move to the beginning of the list
        else:
            index += 1
    print myList[index]


print"OK. Good bye. "






