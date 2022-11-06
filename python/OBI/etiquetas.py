N, K, C = [int(i) for i in input().split()]
fita = [int(i) for i in input().split()]

big = [0,C]
for i in range(K):
    for i in range(len(fita)-C):
        if sum(fita[i:i+C]) <= sum(fita[big[0]:big[1]]):
            big = [i,i+C]
    del fita[big[0]:big[1]]
    big = [0, C]

print(sum(fita))