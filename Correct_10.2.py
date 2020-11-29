initial = input('Enter a File Name: ')
try:
    readable = open(initial)
except:
    print('File Cannot be Opened')
    exit()

time = dict()
for line in readable:
    if line.startswith('From '):
        line = line.split()
        hrs = line[5]
        hrs = hrs[:2]
        time[hrs] = time.get(hrs, 0) + 1

lst = list()
for key, val in time.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for val, key in lst [:9001] :
    print(val, key)
