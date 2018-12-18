#Base Code of project written in Python 3

import binascii
import re
import random
import dnaEncoder as de

BIGCOUNT = 0
div = 0
effcount = 0


while (BIGCOUNT < 10):
    n = 2
    #Uses DNAEncoder class to slim down encoding process in efficiency test
    randString = de.DNAEncoder()
    randString.normalize('The quick brown fox jumps over the lazy dog THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!!@#$%^&*()<>?:"{} . , / \ |[] 0 1 2 3 4 5 6 7 8 9 + - _ = ~ `')
    randString.convert()
    newArray = randString.getNucleotideArray()

    lengthArray = len(newArray)
    knownArray2 = list(newArray)

    #Adds the 12 nucleotide sequence to reduce errors
    count = 24
    con = 1
    while count < len(newArray):
        if con == 1:
            newArray.insert(count,'T')
            con = con + 1
            count = count + 1
        elif con == 12:
            newArray.insert(count,'T')
            con = con + 1
            count = count + 1
        elif con <= 12:
            newArray.insert(count, 'A')
            con = con + 1
            count = count + 1
        else:
            count = count + 24
            con = 1

    lengthArray = len(newArray)

    knownArray = []
    knownArray = list(newArray)


    #TO-DO remove this and add to new file
    #Adds mutations to genetic code
    newCount = 0
    counter = 0
    mutationsCount = 0
    while newCount <= len(newArray):
        while counter <= 23 and newCount < len(newArray):
            randVal = int(random.randrange(0, 4))
            if randVal == 1:
               mu = 'A'
            elif randVal == 2:
               mu = 'T'
            elif randVal == 3:
                mu = 'G'
            else:
                mu = 'C'

            rand = int(random.randrange(0, 1001))
            mutation1 = int(random.randrange(0, 1001))
            if (rand == mutation1):
                if (mutation1 == 2):
                    newArray.pop(newCount)
                    counter = counter +1
                    mutationsCount = mutationsCount +1
                elif (mutation1 == 4):
                    newArray.insert(newCount, mu)
                    newCount = newCount + 1
                    mutationsCount = mutationsCount +1
                else:
                    newArray.insert(newCount, mu)
                    newArray.pop(newCount+1)
                    newCount = newCount + 1
                    counter = counter +1
                    mutationsCount = mutationsCount +1
            else:
                newCount = newCount + 1
                counter = counter + 1
        newCount = newCount + 13
        counter = 1




    deCount = 0
    deCount2 = 0
    while deCount <= (len(newArray)- 24):
        if (newArray[deCount]=='T' and newArray[deCount+1]=='A' and newArray[deCount+2] and newArray[deCount+3]=='A' and newArray[deCount+4] and newArray[deCount+5]=='A' and newArray[deCount+6] and newArray[deCount+7]=='A' and newArray[deCount+8] and newArray[deCount+9]=='A' and newArray[deCount+10]== 'A' and newArray[deCount+11] == 'T'):
            if deCount2 == 24:
                deCount = deCount + 12
                deCount2 = 0


            elif deCount2 < 24:
                newArray.insert(deCount, 'A')
                deCount = deCount + 1
                deCount2 = deCount2 + 1

            elif deCount2 > 24:
                newArray.pop(deCount - 1)
                deCount = deCount - 1
                deCount2 = deCount2 - 1


        else:
            deCount = deCount + 1
            deCount2 = deCount2 + 1


    new = 1
    efCount = 0
    while new <= len(knownArray)-1 and new <= len(newArray)-1:
        if knownArray[new] == newArray[new]:
            efCount = efCount + 1
            new = new + 1
        else:
            new = new + 1


    efCount = float(efCount / (len(knownArray)-1)*100)

    codeCount = 24
    counter11 = 1

    while (codeCount < len(newArray)):
        while counter11 <= 12:
            newArray.pop(codeCount)
            counter11 = counter11 + 1
        codeCount = codeCount + 24
        counter11 = 1


    new = 0
    efCount = 0
    while new <= len(knownArray2)-1 and new <= len(newArray)-1:
        if knownArray2[new] == newArray[new]:
            efCount = efCount + 1
            new = new + 1
        else:
            new = new + 1


    efCount = float(efCount / (len(knownArray2))*100)
    div = div + 1
    effcount = effcount + efCount
    BIGCOUNT = BIGCOUNT + 1
    print(BIGCOUNT)


effiency = effcount/div
print (effiency)
