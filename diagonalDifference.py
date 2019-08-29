def diagonalDifference(arr):
    PriDia=[]
    SecDia=[]
    index = 0
    index_row = len(arr)-1
    for element in range(len(arr)):
        Privalue = arr[element][index]
        PriDia.append(Privalue)
        Secvalue = arr[index_row][index]
        SecDia.append(Secvalue)
        index+=1
        index_row-=1
    PriDiaSum = sum(PriDia)
    SecDiaSum = sum(SecDia)
    DiaDiff = abs(PriDiaSum - SecDiaSum)
    return DiaDiff


arr=[[11,2,4],
     [4,5,6],
     [10,8,-12]]
print(diagonalDifference(arr))