
f = open("input.txt",'r')
illegal = 0
for line in f:
    l = line.split()
    l = [int(x) for x in l]
    print(l)
    dir = l[0] - l[1]
    for x in range(len(l)-1):
        v = l[x] - l[x+1]
        if abs(v) > 3 or abs(v) < 1 or dir * v < 0:
            illegal +=1

            break
        dir += v

print(1000-illegal)
