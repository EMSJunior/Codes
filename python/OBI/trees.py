n = int(input())

trees = [int(i) for i in input().split()]
leni = sum(trees)
area= [0 for i in range(leni)]

j=0
for i in trees: 
    area[j] = 1
    j += i
area.append(1)

resp = 0

for i in range(leni):
    if area[i] == area[-1][i]:
        resp+=1
print(resp)