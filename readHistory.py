def readHistory():
    historyFile = open("history.txt", "r")
    historyList = historyFile.readlines()
    historyFile.close()
    for i in historyList:
        i[len(i)-1] = ""
        print i

    print historyList