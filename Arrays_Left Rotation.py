#Arreglo de pruebasa
arreglo_prueba=[1, 2, 3, 4, 5]
entero_prueba=6

def rotLeft(a, d):
    # Write your code here
    a_rot=a.copy()
    movimiento=d%len(a)
    recuento=0
    for i in range (len(a)):
        if i+movimiento >= len(a):
            a[i]=a_rot[i+movimiento-len(a)]
        else:
            a[i]=a_rot[i+movimiento]
    return a

print(rotLeft(arreglo_prueba,entero_prueba))


"""
si la longitud del arreglo es menor al numero de vueltas entonces




"""
