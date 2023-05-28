mode = 0
numlist = []
roundNeed = 0

def getMod():
    global mode
    wait = 1
    while wait == 1:
        mode = int(input())
        if mode == 1:
            wait = 0
            mode = 1
            print("[1] Generate a list of Fibonacci Number")
        elif mode == 2:
            wait = 0
            mode = 2
            print("[2] Get nth number in the Fibonacci Number")
        else:
             print ("Hmm what do you mean?")

def Start():
    print("Hi, Welcome to Fibonacci Number. What do you want to do?")
    print("[1] Generate a list of Fibonacci Number")
    print("[2] Get nth number in the Fibonacci Number")
    wait = 1
    getMod()

def Generate():
    exnum = 1
    exnum2 = 1
    currentnum = 1
    num = 1
    wait = 1
    global roundNeed
    numlist = []
    print("How many digits do you want? 0 to exit")
    wait = 1
    while wait == 1:
        global roundNeed
        roundNeed = int(input())
        if roundNeed != 0:
            print("Ok, here you go.")
            wait = 0
        else:
            print("I guess you do not need any...")
            roundNeed = 0
            wait = 0
            exit()
    while roundNeed != 0:
        numlist.append(num)
        currentnum = num
        num = currentnum + exnum
        exnum = exnum2
        exnum2 = num
        roundNeed = roundNeed - 1
    print(numlist)

def nth():
    exnum = 1
    exnum2 = 1
    currentnum = 1
    num = 1
    wait = 1
    global roundNeed
    numlist = []
    print("What digit do you want? 0 to exit")
    wait = 1
    while wait == 1:
        global roundNeed
        roundNeed = int(input())
        if roundNeed != 0:
            
            wait = 0
        else:
            print("I guess it is 0")
            roundNeed = 0
            wait = 0
            exit()
    listcount = roundNeed - 1
    while roundNeed != 0:
        numlist.append(num)
        currentnum = num
        num = currentnum + exnum
        exnum = exnum2
        exnum2 = num
        roundNeed = roundNeed - 1
    print("Ok, here you go. It's", numlist[listcount])


Start()
print (mode)
wait = 1
while wait == 1:
    if mode == 1:
        wait = 1
        Generate()
    elif mode == 2:
        wait = 1
        nth()

