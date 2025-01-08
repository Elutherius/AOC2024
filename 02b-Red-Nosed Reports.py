
f = open("input.txt",'r')
illegal = 0
for line in f:
    l = line.split()
    l = [int(x) for x in l]
    prob = False
    dir = 0
    x = 0
    print(l)
    while x < len(l)-1:

        v = l[x] - l[x+1]
        if v != 0:
            dir += (abs(v) / v)
        x += 1
    if abs(dir) < len(l) - 3:
        illegal +=1
    else:
        x = 0
        while x < len(l)-1:
            v = l[x] - l[x+1]
            print(v)
            if abs(v) > 3 or abs(v) < 1 or dir * v < 0:
                if not prob and x < len(l)-2:
                    print(x)
                    v = l[x] - l[x+2]
                    if abs(v) > 3 or abs(v) < 1 or dir * v < 0:
                        l.remove(l[x])
                        x = max(x-1,0)
                    else:
                        l.remove(l[x+1])
                        x+=1
                    prob = True
                elif x == len(l)-2 and not prob:
                    break
                else:
                    illegal +=1
                    break
            else:
                x += 1
print(1000-illegal)
