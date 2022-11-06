from operator import indexOf


#ij = [int(i) for i in input().split()]
#
#malha = [input().split() for i in range(ij[0])]
#sumsh = [int(i[-1]) for i in malha]
#
#sumsv = [int(i) for i in input().split()]

ij= [4,5]
alfa = [["df", "bb", "cg", "df", "df", 11],
["ee", "az" ,"cg","az","ee", 6],
["df", "cg", "cg", "df", "df", 10],
["az", "az", "cg", "az", "az", 6]]
sumsh = [int(i[-1]) for i in alfa]
malha = [i[:-1] for i in alfa]
sumsv = [6, 7, 8, 6, 6]

resp = {}

resp[189] = 18 
 
for i in range(0,malha):
    if set(malha[i]) == malha[i]:
        resp[i[0]] = sumsh[i] / ij[1]

print(resp)
