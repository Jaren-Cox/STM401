import re
op = open('mbox-short.txt')
inpu = input('Enter a Regular Expression: ')
count = 0
for line in op:
    line = line.rstrip()
    word = re.findall(inpu, line)
    if len(word) > 0:
        count = count + 1
print('mbox had', count, 'lines that contained', inpu)