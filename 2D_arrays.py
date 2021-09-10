imput = [[0 ,-4 ,-6 ,0,-7,-6]
    ,[-1, -2, -6, -8, -3, -1]
    ,[-8, -4, -2, -8, -8, -6]
    ,[-3, -1, -2, -5, -7, -4]
    ,[-3, -5, -3, -6, -6, -6]
    ,[-3, -6, 0 ,-8 ,-6 ,-7 ]]

def hourglassSum(arr):
    suma=None
    # Write your code here
    for i in range(len(arr[0])-2):
        for j in range(len(arr)-2):
            arriba=(arr[i][j])+(arr[i][j+1])+(arr[i][j+2])
            medio=arr[i+1][j+1]
            abajo=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sumatoria=arriba+medio+abajo
            if suma== None:
                suma=sumatoria
            elif suma<sumatoria:
                suma=sumatoria
    print(arriba,abajo,medio)
    return suma
            


print(hourglassSum(imput))