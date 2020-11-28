txt = open('mbox.txt')
for lx in txt:
    line = lx.rstrip()
    print(line.upper())