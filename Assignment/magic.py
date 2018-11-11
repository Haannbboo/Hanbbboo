import numpy
import os


def Qone(K=3,P=1):
    while K>1:
        print(K)
        K-=1
        P*=K
    return P

class magic(object):
    def ismagic(array):
        '''array: numpy.array object'''
        try:
            shape=array.shape
        except Exception:
            raise TypeError("input should be numpy.array, not "+str(type(array)))
        if shape[0]!=shape[1]:
            raise ValueError("Not a square array")
        s=(shape[0]*shape[0]+1)*shape[0]/2
        diag1,diag2,row,col=0,0,0,0
        for i in range(shape[0]):
            diag1+=array[i][i]
            diag2+=array[i][-i-1]
            for j in range(shape[1]):
                row+=array[i][j]
                col+=array[j][i]
            if row==s and col==s:
                #print(row,col)
                row,col=0,0
            else:
                return "Not a magic array1"
        if diag1==s and diag2==s:
            return "Magic array"
        else:
            return "Not a magic array2"
    def generate(n):
        '''n: col & row number of the square array'''
        if n%2==0:
            return "n must be an odd number"
        m=numpy.zeros(n*n).reshape(n,n)
        z=1
        h,v=0,n//2
        m[h][v]=1
        while True:
            z+=1
            if z==n*n+1:
                break
            while m[(h-1)%n][(v+1)%n]!=0:
                #print(h,v)
                h=h+1
                m[h][v]=z
                z+=1               
            h=(h-1)%n
            v=(v+1)%n
            m[h][v]=z
            #print(m)
        return m




##########
    #Play part
##########

realPath=os.path.realpath(__file__)
