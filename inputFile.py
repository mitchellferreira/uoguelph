#!/usr/bin/python

import inputString

def getFile(filePath):
    returnList = ["FILE_R"]

    try:
        file inputFile = open(filePath, 'r')
    except IOError:
        logger(["ERROR","Could not open input file, IOError exception."])
        return ["ERROR","Could not open input file."]

    for line in inputFile:
        if(len(line) != 0):
            tempList = parseInputString(line)
            if(tempList == None):
                logger(["ERROR","parseInputString return a None object when reading the input file."])
                continue
            else:
                returnList.append(tempList)

    return returnList
    
