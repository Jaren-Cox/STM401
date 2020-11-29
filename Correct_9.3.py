initial = input('Enter a File Name: ')
try:
    readable = open(initial)
except:
    print('File Cannot be Opened')
    exit()

people = dict()
for line in readable:
    if line.startswith('From '):
        line = line.split()
        person = line[1]
        people[person] = people.get(person, 0) + 1
print(people)
