#!/usr/bin/python

list = ["GOOD", "hi"]

def inputHandler(path):
	if (path == "std" or path == "cmd"):
		print "if"
		#call getInputString(path)
	else:
		print "else"
		#call getFunction()

	if (list[0] == "FILE"):
		fileName = list[1]
		#call getFile(fileName)
		print "file"

	elif (list[0] == "GOOD"):
		equation = list[1]
		#call mathHandler(path, equation)
		print "good"

	elif (list[0] == "GRAPH"):
		equation = list[1]
		#call graphHandler(equation)
		print "graph"

	#if first element is ERROR
	else:
		message = list[1]
		#call printError(path, message)
		print "else"

inputHandler("cmd");
