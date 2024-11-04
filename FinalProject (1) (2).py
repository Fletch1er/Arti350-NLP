
#Puts the nodes in a list and Counts the occurences
def nodeCount(file):
    nodeList = []
    nonRepeatList = []
    try:
        with open(file, "r") as myFile:
            fileContents = myFile.readlines()
    except FileNotFoundError:
        fileError()
    try:
        for item in fileContents:
            nodeFind = item.find(" - ")
            nodeList.append(item[0:nodeFind])
        for item in nodeList:
            if item not in nonRepeatList:
                nonRepeatList.append(item)
        nonRepeatList.sort()
        for item in nonRepeatList:
            count = nodeList.count(item)
            print(item + ": " + str(count))
    except UnboundLocalError:
        unboundE()
#Gets the ip address then matches the 2nd and 3rd value with the input
def octetFind(file):
    octetlist = []
    octetValue = input("Please enter an Octet:")
    try:
        with open(file, "r") as myFile:
            fileContents = myFile.readlines()
    except FileNotFoundError:
        fileError()
    try:
        for item in fileContents:
            firstSplit = item.find(" - ")
            secondSplit = item.rfind(" - ")
            octetlist.append(item[firstSplit + 3:secondSplit])
        for item in octetlist:
            ipAdress = item.split(".")
            if octetValue == ipAdress[1] or octetValue == ipAdress[2]:
                print(item)
    except UnboundLocalError:
        unboundE()
#Finds the first octet value, then counts how many time each individual occurs
def firstOctetCount(file):
    octetList = []
    firstOctetList = []
    uniqueOctet = []
    try:
        with open(file, "r") as myFile:
            fileContents = myFile.readlines()
    except FileNotFoundError:
        fileError()
    try:
        for item in fileContents:
            firstSplit = item.find(" - ")
            secondSplit = item.rfind(" - ")
            octetList.append(item[firstSplit + 3:secondSplit])
        for item in octetList:
            firstOctet = item.find(".")
            firstOctetList.append(item[0:firstOctet])
        for item in firstOctetList:
            if item not in uniqueOctet:
                uniqueOctet.append(item)
        for item in uniqueOctet:
            count = firstOctetList.count(item)
            print(item + ": " + str(count))
    except UnboundLocalError:
        unboundE()
#Finds the unique message inputs and counts their occurences
def messageFind(file):
    messageList = []
    uniqueMessageList = []
    try:
        with open(file, "r") as myFile:
            fileContents = myFile.readlines()
    except FileNotFoundError:
        fileError()
    try:
        for item in fileContents:
            noNewLine = item.replace("\n", "")
            messageFind = noNewLine.rfind("User")
            messageList.append(noNewLine[messageFind:])
        for item in messageList:
            if item not in uniqueMessageList:
                uniqueMessageList.append(item)
        for item in uniqueMessageList:
            count = messageList.count(item)
            print(item + ": " + str(count))
    except UnboundLocalError:
        unboundE()
def unboundE(): #except unbound variable error
    with open("finalProjExceptions.txt", "a") as myFile:
             print("Variable does not exist")
             myFile.write(" List not yet assigned.")
             
def fileError(): #except for file not found error
    with open("finalProjExceptions.txt", "w") as myFile:
        print("File does not exist!")
        myFile.write(" File was not found.")
        

def FinalProjectFunc():
    userFile = input("Enter a text file to be analyzed: ")
    task = int(input("What task would you like to complete?"))
    if task == 1:
        nodeCount(userFile)
    elif task == 2:
        octetFind(userFile)
    elif task == 3:
        firstOctetCount(userFile)
    elif task == 4:
        messageFind(userFile)
    
FinalProjectFunc()