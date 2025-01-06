import numpy as np


def khayam(n):

    mat = np.zeros((n, n), np.int64)


    for i in range(n):
        for j in range(n):
   
            if j==0 or i==j:
                mat[i,j] =1 
            else:
                mat[i,j]= mat[i-1,j] + mat[i-1,j-1]

    return mat


print(khayam(5))