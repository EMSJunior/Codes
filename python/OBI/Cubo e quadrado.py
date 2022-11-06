r = 0
for i in range(int(input()),int(input()) + 1):
    if format((i**(1/3)),'.15f')%1 == 0:
        if format((i**(1/2)),'.15f')%1 == 0:
            r += 1     

print(r)