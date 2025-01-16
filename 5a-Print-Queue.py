f = open("input1.txt", "r")
pastRules = False
rules = {}
count = 0
for line in f:
    if not pastRules:
        if line == "\n":
            pastRules = True
        else:
            temp = line.strip().split("|")
            if (temp[1]) not in rules:
                rules[(temp[1])] = [(temp[0])]
            else:
                rules[(temp[1])].append((temp[0]))
    else:
        tempLine = line.strip().split(",")
        good = True
        x = 0

        found = False
        for x in range(len(tempLine)):
            for y in range(x + 1, len(tempLine)):
                if tempLine[y] in rules.get(tempLine[x], {}):
                    good = False
                    found = True
                    break
            if found:
                break
        if good:
            count += int(tempLine[len(tempLine)//2])



print(count)



