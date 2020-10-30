time=input('Worked hours?')
timenumb=int(time)
pay=input('Pay per hour?')
paynumb=int(pay)
if paynumb >= 40:
    print('Your Pay is: $',(1.5*paynumb)*timenumb)
else:
    print('Your pay is: $', paynumb*timenumb)
