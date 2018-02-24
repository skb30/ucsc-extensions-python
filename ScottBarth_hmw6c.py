# String challenge - Extra Extra chanllenge

def myCountSubstringInString(findString, targetString):
    count = 0
    findStringLength = len(findString)

    if findStringLength == 1: # easy path, if findstring is only 1 char
        for char in targetString:
            if char == findString:
                count += 1
    else: # time to do some work
        for index in range(0,len(targetString)):
            if targetString[index:index + len(findString)] == findString:
                count += 1
    return count


# this version uses the built in {mylist}.count method
def countSubstringInString(findString, targetString):
    return targetString.count(findString)



print "The number of occurences ", myCountSubstringInString('a', "bananarama") # excpect 5
print "The number of occurences ", myCountSubstringInString('ama', "bananarama") # excpect 1
print "The number of occurences ", myCountSubstringInString('an', "bananarama") # excpect 2
print "The number of occurences ", myCountSubstringInString('aaaaaaaaaaaaaaaaaaaa', "bananarama") # excpect 0

print "The number of occurences ", countSubstringInString('a', "bananarama") # excpect 5
print "The number of occurences ", countSubstringInString('ama', "bananarama") # excpect 1
print "The number of occurences ", countSubstringInString('an', "bananarama") # excpect 2
print "The number of occurences ", countSubstringInString('aaaaaaaaaaaaaaaaaaaa', "bananarama") # excpect 0














