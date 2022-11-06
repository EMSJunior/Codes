a, b = [input(), input()]
lena, lenb = [len(a), len(b)]
size = lena

if lena > lenb:
    for i in range(lena - lenb):  
        b = "0" + b
    size = lena
elif lenb > lena:
    for i in range(lenb - lena):
        a = "0" + a
    size = lenb

f=["",""]
  
for i in range(size):
    if int(a[i]) > int(b[i]):
        f[0] += a[i]
    elif int(b[i]) > int(a[i]):
        f[1] += b[i]
    else:
        f[0] += a[i]
        f[1] += b[i]
if f[0] == "":
    f[0] = "-1"
if f[1] == "":
    f[1] = "-1"

r = sorted(f)       
print(int(r[0]), int(r[1]))