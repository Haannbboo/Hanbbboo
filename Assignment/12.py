import numpy as np

def generate(size):
    mat=np.random.randint(0,3,size)
    print("The initial array with 0s")
    print(mat)
    return mat

def compress(size):
    '''size -> an integer to generate a size*size shape array'''
    mat=generate(size)
    #mat=[[7,0,0,0,0,0],[0,0,0,0,0,0],[0,0,-3,0,9,0],[0,0,0,0,0,0],[0,0,-1,0,0,0],[0,-6,0,0,-5,-1]]
    count=0
    K=0
    VALUES,COL,ROWC=[],[],[0]*len(mat)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0:
                VALUES.append(0)
                VALUES[K]=mat[i][j]
                COL.append(0)
                COL[K]=j
                K+=1
                count+=1
        ROWC[i]=count
    return VALUES,COL,ROWC

#values,col,rowc=compress(5)

#################################################################################################
from pythonds.basic.stack import Stack
a=Stack()
names=['theta','lambda','zeta','epsilon','delta','gamma','mu','alpha']
for i in reversed(names):
    a.push(i)

def search(item,a):
    '''item -> item searching
    a -> the target stack'''
    index=0
    while not a.isEmpty():
        X=a.pop()
        #print(X)
        if X==item:
            break
        else:
            index+=1
    if index==a.size():
        return "Not found"
    else:
        return index

class Tree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right
    def left(self):
        return self.left
    def right(self):
        return self.right
    def cargo(self):
        return self.cargo


