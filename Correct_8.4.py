txt = open('romeo.txt')
list = []
for line in txt:
    word = line.split(" ")
    for word in word:
        if word not in list:
            lower = word.lower()
            list.append(lower.strip())
list.sort()
print(list)