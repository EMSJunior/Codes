N = int(input())
num = [int(i) for i in input().split()]


zero = [0] * N
cinco = [0] * N
rzero = [0] * N
rcinco = [0] * N
azero = False
arzero = False
acinco = False
arcinco = False

for i in range(N):
    if num[i] == 0 and not azero:
        zero =  num[:i] + [num[-1]] + num[i+1:-1] + [0]
        azero = True
    elif num[i] == 5 and not acinco:
        cinco = num[:i] + [num[-1]] + num[i+1:-1] + [5]
        acinco= True
        
for i in range(N-1,0,-1):
    if num[i] == 0 and not arzero:
        rzero =  num[:i] + [num[-1]] + num[i+1:-1] + [0]
        arzero = True
    elif num[i] == 5 and not arcinco:
        rcinco = num[:i] + [num[-1]] + num[i+1:-1] + [5]
        arcinco= True


if azero or acinco:
    n = ["", "","",""]
    
    for i in range(N):
        n[0] += str(zero[i])
        n[1] += str(cinco[i])
        n[2] += str(rcinco[i])
        n[3] += str(rzero[i])
    resp = 0
    for i in n:
        if int(i) > int(resp):
            resp = i
    
    for i in resp:
        print(i + " ", end=" ")
else:
    print(-1)
    
    