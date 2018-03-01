import random
import time
import sys

reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', \
              'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries', \
              'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7']

nPicturesInReel = len(reelList)

nCoins = 100
print 'You have', nCoins, 'coins to start.  Good luck.'
print
nCoinsWon = 0
def payTable(myList):
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]

    # the user has 3 of a kind. determine which kind.
    if myList.count(picture1) == 3:
        if picture1 == 'Lucky 7':
            nCoinsWon = 500
        elif picture1 == 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10

    else:
        if (picture1 == picture2) or (picture1 == picture3) or (picture2 == picture3):
            nCoinsWon = 2
        else:
            nCoinsWon = 0

    return nCoinsWon

while True:

    if nCoins == 0:
        print 'Sorry to see you go.  Come back again soon.'
        sys.exit(0)  # New, but works to quit the program

    bet = raw_input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')
    if bet == '':
        bet = 1
    try:
        bet = int(bet)
        pass
    except:
        print "You must enter a positive int"
        continue

    if bet < 0:
        print "You must enter a positive int"
        continue

    if bet > nCoins:
        print "Sorry, you do not have that many coins, you only have: ", nCoins
        continue

    if bet == 0:
        sys.exit(0)

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print 'Spinning ... '
    print
    time.sleep(.5)
    print '     ', resultList[0]
    time.sleep(.5)
    print '     ', resultList[1]
    time.sleep(.5)
    print '     ', resultList[2]
    print

    nCoins = nCoins - bet
    payOut = bet * payTable(resultList)

    if payOut == 0:
        print 'Sorry - you lose.'

    else:
        print 'You won', payOut, 'coins.  Cha-ching!'
        if payOut and payOut > 50:
            print '                         WOOOOO  HOOOOOOOOOOO!!!!'

    nCoins = nCoins + payOut

    print 'You now have ' + str(nCoins) + ' coins.'
    print

