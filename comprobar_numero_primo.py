
X=(input("ingrese numero que desee comprobar si es primo o no:\n"))
try: X=int(X)
except :X=float(X)

def identificador_primos(num):
    if num == 1:
        return print("no es primo")
    elif num == 2:
        return print("Es primo")
    else:
        for i in range(2,num):
            if num%i == 0:
                return print("no es primo")
        return print("Es primo")

#for i in range(1, 101): #prueba
#    print(i)
#    identificador_primos(i)
