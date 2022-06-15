def soma(n1,n2):
        return int(n1)+int(n2)
def subt(n1,n2):
    return int(n1)-int(n2)
def mult(n1,n2):
    return int(n1)*int(n2)
def divi(n1,n2):
    return int(n1)/int(n2)
while(1):
    print("\n------------------------------\nBem vindo a calculadora em .py\n------------------------------")
    n1, s, n2 = input("Operação: ").split()

    if s == "+":
        print(n1, s, n2, "=", soma(n1,n2))
    if s == "-":
        print(n1, s, n2, "=", subt(n1,n2))
    if s == "*":
        print(n1, s, n2, "=", mult(n1,n2))
    if s == "/":
        print(n1, s, n2, "=", divi(n1,n2))

    escolha = input("Colocar mais um número? (s/n)")
    if escolha  == "n":
        break
