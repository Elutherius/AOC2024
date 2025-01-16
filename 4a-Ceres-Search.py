def xFinder(array):
    count = 0
    for line in array:
        while(True):
            xmind = line.find("XMAS")
            saind = line.find("SAMX")
            if xmind > saind and (xmind != -1 and saind !=-1):
                count +=1
                line = line[saind+3:]
            elif saind > xmind and (xmind !=-1 and saind !=-1):
                count +=1
                line = line[xmind+3:]
            elif (xmind != -1 or saind !=-1):
                count +=1
                line = line[max(xmind,saind)+4:]
            else:
                break
    return count


f = open("input1.txt", "r")
count = 0
lines = [line.strip() for line in f.readlines()]
print(lines)

vert = ["" for _ in range(len(lines[0]))]
print(vert)
for line in lines:
    for i, c in enumerate(line):
        vert[i] +=c

dia1 = ["" for _ in range(len(lines[0]) + len(lines) - 1)]


x = len(lines[0])
y = 0


for j, line in enumerate(lines):
    y = j
    for i in range(x-1,-1,-1):
        dia1[y] += line[i]
        y+=1

dia2 = ["" for _ in range(len(lines[0]) + len(lines) - 1)]




for j, line in enumerate(lines):
    y = j
    for i in range(x):
        dia2[y] += line[i]
        y+=1




count += xFinder(lines)
count += xFinder(vert)
count += xFinder(dia1)
count += xFinder(dia2)
print(count)
