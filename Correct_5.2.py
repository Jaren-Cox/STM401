number = 0
total = 0.0
largest = None
smallest = None
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
    if largest is None:
        largest = numbs
    elif numbs > largest:
        largest = numbs
    if smallest is None:
        smallest = numbs
    elif numbs < smallest:
        smallest = numbs
print('Sum: ', total, 'Number of Numbers: ', number, 'Largest Number: ', largest, 'Smallest Number:', smallest)