#!/usr/bin/python

import sys
import os

def getInputString(location):
    if(location == cmd):
        inputString = raw_input("Please enter your function: ")
    elif(location == std):
        TODO;
    else:
        logger(["ERROR","getInputString received an invalid parameter."])
        return ["ERROR","Something went wrong when we tried to evaluate your equation.")
    
    parsedString = parseInputString(inputString)
    if(parsedString == None or len(parsedString) == 0):
        logger(["ERROR","parseInputString() failed to return a value"])
        return ["ERROR","Something went wrong when we tried to evaluate your equation.")
    else:
        return parsedString

def parseInputString(inputString):
    validChars = ['pow', '^', 'sin', 'cos', 'tan', 'csc', 'sec', 'cot', 'asin', 'acos', 'atan', 'acsc',
                  'asec', 'acot', 'e', 'pi', '.', '+', '/', '\\', '*', '%', '-', 'log', 'ln', 'sqrt',
                  '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!']
    inputStringTemp = ''
    
    inputFile = os.path.isfile(inputString)
    if(inputFile):
        if(inputString.endsWith(".txt")):
           return ["FILE",inputString]
        else:
           return ["ERROR","Please ensure your input file is a .txt file."]

    inputString.replace('\\','/')
    inputString.strip()
    inputString.replace(' ','')
        
    leftBracket = 0
    rightBracket = 0
    for character in inputString:
        if(character == '('):
            leftBracket += 1
            continue
        elif(character == ')'):
            rightBracket += 1
            continue
        else:
            continue
    if(rightBracket != leftBracket):
        return ["ERROR","The equation you input does not have a matching number of brackets!"]

    inputStringTemp = inputString
    for element in validChars:
        inputStringTemp.replace(element, '')
    if(len(inputStringTemp) != 0):
        return ["ERROR","The equation you have input contains one or more invalid expressions: " + inputStringTemp]

    for character in inputString:
        if(character == '+' or character == '-' or character == '/' or character == '*' or character == '%'):
            if(operator == True):
                return ["ERROR","The equation you have inpute contains one or more instances of adjacent operators. eg. +*"]
            else:
                operator = True
                continue
        if(operator == True):
            operator = False

    return ["GOOD",inputString]
        
    
    
        
