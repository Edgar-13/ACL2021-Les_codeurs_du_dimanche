def PLSC_recursif(i,j):
    if i==-1 or j==-1:
        return 0
    else:
        if L1[i-1]==L2[j-1]:
            return 1+PLSC_recursif(i-1,j-1)
        else :
            return max(PLSC_recursif(i-1,j),PLSC_recursif(i,j-1))

L1="pour"
L2="poupou"
i = len(L1)-1
j = len(L2)-1

import numpy as np

def PLSC_dynamique(L1,L2):
    m=len(L1); n=len(L2)
    c = np.zeros((n,m))
    b = np.zeros((n,m))
    for i in range (1,m):
        for j in range(1,n):
            if L1[i]==L2[j]:
                c[i,j]=c[i-1,j-1]+1
                b[i,j]=0
            elif c[i-1,j]>=c[i,j-1]:
                c[i,j]=c[i-1,j]
                b[i,j]=1
            else:
                c[i,j]=c[i,j-1]
                b[i,j]=2
    return c,b


def PLSC_dyn2(L1,b,i,j):
    if i <= 1 or j <=1:
        return ['.']
    if b[i,j]==0:
        PLSC_dyn2(L1,b,i-1,j-1)
        print(L1[i])
    elif b[i,j]==1:
        PLSC_dyn2(L1,b,i-1,j)
    else:
        PLSC_dyn2(L1,b,i,j-1)


b = PLSC_dynamique(L1,L2)[1]

PLSC_dyn2(L1,b,i,j)
