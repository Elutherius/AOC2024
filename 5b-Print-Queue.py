f = open("input.txt", "r")
pastRules = False
rules = {}
count = 0
for line in f:
    if not pastRules:
        if line == "\n":
            pastRules = True
            print(rules)
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
        if not good:
            stack = []
            final = []
            while tempLine:
                stack.append(tempLine.pop(0))
                while stack:
                    print(stack)

                    if stack[-1] in rules:
                        print(f"{stack} in rules")
                        print(tempLine)
                        flag = False
                        for x in range(len(tempLine)):
                            print(tempLine[x])
                            if tempLine[x] in rules.get(stack[-1], {}):
                                stack.append(tempLine.pop(x))
                                flag = True
                                break
                        if not flag:
                            print(f"{final} final")
                            final.append(stack.pop(-1))
                    else:
                        final.append(stack.pop(-1))


            print(final)
            count += int(final[len(final)//2])


print(count)



