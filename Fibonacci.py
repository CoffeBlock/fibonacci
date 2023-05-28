import time
start = 1
exnum = 1
exnum2 = 1
cerrentnum = 1
num = 1
wait = 1
roundNeed = 0

print("How many digits do you want?")
while wait == 1:
        roundNeed = int(input())
        if roundNeed != 0:
            print("Ok, here you go.")
            wait = 0
        else:
            print("I guess you do not need any...")
            wait = 0

while roundNeed != 0:
        print(num)
        cerrentnum = num
        num = cerrentnum + exnum
        exnum = exnum2
        exnum2 = num
        roundNeed = roundNeed - 1
        time.sleep(0.5)
