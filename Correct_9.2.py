initial = input('Enter a File Name: ')
try:
    readable = open(initial)
except:
    print('File Cannot be Opened')
    exit

dates = dict()
for line in readable:
    if line.startswith('From '):
        line = line.split()
        date = line[2]
        dates[date] = dates.get(date, 0) + 1
print(dates)