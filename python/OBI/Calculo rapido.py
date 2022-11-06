S = int(input())
A = int(input())
B = int(input())

resp = 0

for i in range(A,B+1):
    if (sum(int(x) for x in str(i))) == S:
        resp += 1
print(resp)