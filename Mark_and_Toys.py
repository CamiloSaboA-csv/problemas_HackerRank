def maximumToys(prices, k):
    
    prices=sorted(prices)
    cantidad_objetos=0
    suma_precio_juguetes=0

    for i in prices:
        if suma_precio_juguetes<k:
            suma_precio_juguetes+=i
            if suma_precio_juguetes<=k:
                cantidad_objetos+=1
            else: break
    return cantidad_objetos
        


a,b=[3, 7, 2, 9, 4], 15

x=100000000

x=maximumToys(a,b)

print(x)