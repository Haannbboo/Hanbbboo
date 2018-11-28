class Tree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def _str_(self):
        return str(self.data)

def postPrint(tree):
    if tree is None:
        return
    postPrint(tree.left)
    postPrint(tree.right)
    print(tree.data,end=" ")
def inPrint(tree):
    if tree is None:
        return
    inPrint(tree.left)
    print(tree.data,end=" ")
    inPrint(tree.right)
def prePrint(tree):
    if tree is None:
        return
    print(tree.data,end=" ")
    prePrint(tree.left)
    prePrint(tree.right)
