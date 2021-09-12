def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    
    for pos, val in enumerate(arr):
        print(val,pos)
        temp[val] = pos
        pos += 1                    #! creamos un arreglo de 0's
    #print(temp)
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            print(arr)
            arr[temp[i+1]] = t
            print(arr)
            temp[t] = temp[i+1]
    #print(swaps)
    return swaps


a=[5,4,2,3,1]
minimumSwaps(a)


