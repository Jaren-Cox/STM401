import time
tim=input('Hours worked?')
try:
    clock=int(tim)
except:
    print('Not a number')
    time.sleep(5)
    quit('Not a number')
mon=input('Payment per hour?')
try:
    monee=int(mon)
except:
    print('Not a number')
    time.sleep(5)
    quit('Not a number')
print("Your pay should be $", clock*monee)
