


f = open("input1.txt", "r")
count = 0
lines = [line.strip() for line in f.readlines()]
print(lines)



print(len(lines[0]))
print(len(lines))
for i in range(1,len(lines[0])-1):
    for j in range(1,len(lines)-1):
        print(f"i is {i} and j is {j}")
        if lines[i][j] == 'A':
                if ((lines[i-1][j-1], lines[i+1][j+1]) in [('S', 'M'), ('M', 'S')] and
                    (lines[i-1][j+1], lines[i+1][j-1]) in [('S', 'M'), ('M', 'S')]):
                    count +=1
print(count)
