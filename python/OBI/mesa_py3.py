A = (int(input()) % 3)
B = (int(input()) % 3)
cadeiras = [True, True, True]

cadeiras[A] = False

if cadeiras[B]:
    cadeiras[B] = False
elif B == 2:
    cadeiras[0] = False
else:
    cadeiras[B+1] = False

for i in range(3):
    if cadeiras[i]:
        resp = i
        break;

print(resp)
    