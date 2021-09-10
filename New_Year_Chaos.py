
a=[[2, 1, 5, 3, 4],
    [2, 5, 1, 3, 4],
    [5, 1, 2, 3, 7, 8, 6, 4],
    [1, 2, 5, 3, 7, 8, 6, 4],
    [1, 2, 5, 3, 4, 7, 8, 6]]

#a=[[1, 2, 5, 3, 7, 8, 6, 4]]

#3,ToC,toC,7,4


#!Metodo 1 que logra el 60% de los test
def minimumBribes2(q):
    # Write your code here
    sum_movemets=0
    arr=sorted(q.copy())
    #print(f"arreglo: {q}") #! debug
    for i in range(len(arr)):
        contador=0
        #print(arr)
        while arr[i]!= q[i]:
            pos_ini=arr.index(q[i])
            dif=pos_ini-i
            arr.insert(pos_ini-dif,arr.pop(pos_ini))
            contador=contador+dif  
        sum_movemets+=contador
        if contador>=3:
            return print("Too chaotic")
    return print(sum_movemets)

#! Metodo 2, logra el 100% de los test
def minimumBribes(q):
    moves = 0 
    print(q)
    q = [P-1 for P in q] # le quitamos 1 unidad a todos los valores para hacerlos similares a los index
    print(q)
    for i,P in enumerate(q):
        print(P,i)
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1,0),i):
            if q[j] > P:
                moves += 1
    print(moves)

#lista=list(map(minimumBribes,a))
minimumBribes(a[3])