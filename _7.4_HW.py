op = open('romeo.txt')
for lp in op:
    lt = lp.rstrip()
    print(lt.upper())
