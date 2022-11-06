ip = int(input())
passwords = [input() for i in range(ip)]

L = ''
resp = 0
for i in range(ip):
    senha = passwords[i]
    resp += L.count(senha)
    L += senha + ','
    
print(resp )