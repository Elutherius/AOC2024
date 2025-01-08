
f = open("input.txt",'r')
illegal = 0
for line in f:
    l = line.split()
    l = [int(x) for x in l]
    print(l)
    if l[0] < l[-1]:
        for x in range(0,len(l)-1):
            if (l[x+1] - l[x]) > 3 or (l[x+1] - l[x]) < 1:
                print(f"{l[x+1]} - {l[x]} = ")
                illegal +=1
                break
    else:
        for x in range(0,len(l)-1):
            if (l[x] - l[x+1]) > 3 or (l[x] - l[x+1]) < 1:
                print(f"{l[x]} - {l[x+1]} = ")
                illegal +=1
                break

print(1000-illegal)
