number = 0
total = 0.0
while True :
    inpu = input('Enter a Number: ')
    if inpu == 'done':
        break
    try:
        numbs = float(inpu)
    except:
        print('Not a Number')
        continue
    number = number + 1
    total = total + numbs
print('Sum of numbers: ', total,'Number of numbers: ', number,'Average of numbers:', total/number)