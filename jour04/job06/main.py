L=[1,2,3,4,5]
index1=L.index(1)
index2=L.index(5)

L[index1], L[index2]= L[index2] , L[index1]

print(L)