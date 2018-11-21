'''
@ Haannbboo
Created on Nov.21st
:Linked list
'''
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getInit(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,newdata):
        self.next=newdata
    def setInit(self,newinit):
        self.data=newinit
    #def __str__(self):
        #return str(self.data)
    
class Linked:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        '''Linked.isEmpty() -> boolean -- see if linked list is empty'''
        return self.head==None
    def add(self,item):
        '''Linked.add(item) -> None -- add item at the front'''
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        '''Linked.size() -> integer -- get the size of linked list'''
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def search(self,item): 
        '''Linked.search(item) -> boolean -- see if item exists in linked list'''
        current=self.head
        found=False
        while current!=None:
            if current.getInit()==item:
                return True
            else:
                current=current.getNext()
        return False
    def remove(self,item):
        '''Linked.remove(item) -> None -- remove first occurance of item'''
        if not self.search(item):
            raise ValueError("No such item in linked list")
        current=self.head
        previous=None
        while True:
            if current.getInit()==item:
                break
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
    def append(self,item):
        '''Linked.append(item) -> None -- append item to end'''
#        current=self.head
#        if current:
#            while current.getNext()!=None:
#                current=current.getNext()
#            current.setNext(Node(item))
#        else:
#            self.head=Node(item)
        if self.size()==0:
            return self.add(item)
        last=self.Index(-1)
        last.setNext(Node(item))
    def index(self,item):
        '''Linked.index(item) -> integer -- get the index of first met item'''
        if not self.search(item):
            raise ValueError("No such item in linked list")
        current=self.head
        cnt=-1
        while current!=None:
            cnt+=1
            if current.getInit()==item:
                return cnt
            else:
                current=current.getNext()
    def insert(self,pos,item):
        '''Linked.insert(pos,item) -> None -- insert item before index pos'''
#        current=self.head
#        i=0
#        if pos==0:
#            self.add(item)
#        else:
#            while current!=None and i<pos-1:
#                current=current.getNext()
#                i+=1
        if pos==0:
            self.add(item)
            return
        elif pos<0:
            current=self.Index(pos)
        else:
            current=self.Index(pos-1)
        temp=Node(item) # With indentation with while
        temp.setNext(current.getNext())
        current.setNext(temp)
    def pop(self,pos=-1):
        '''Linked.pop([index]) -> remove and return item at index (default last)'''
#        previous=self.head
#        i=-1
#        if pos==0:
#            item=self.
#        while previous!=None and i<=pos-3:
#            previous=previous.getNext()
#            i+=1

        if pos==0:
            previous=None
        else:
            previous=self.Index(pos-1)
        current=self.Index(pos)
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getInit()
    def Index(self,index):
        '''Linked.Index(index) -> item -- indexing linked list'''
        current=self.head
        i=0
        if not isinstance(index,int):
            raise TypeError("Linked list index must be a integer")
        elif index<0:
            index=self.size()+index
        elif index>=self.size():
            raise IndexError("Linked list index out of range")
        while current!=None and i<index:
            current=current.getNext()
            i+=1
        return current
    def __str__(self):
        current=self.head
        cnt=self.size()
        i=0
        out=''
        while i<=cnt-1:
            out+=str(current.getInit())+', '
            current=current.getNext()
            i+=1
        return out

## Comment within the class means that I literally understand how the method works
## and has come up with a new method to simply it
def test():
    a=Linked()
    print("Testing add: a.add(item)")
    a.add(30),a.add(40),a.add('Hanbo')
    print(a)
    print('\n'+"Testing size: a.size()")
    print("Size: "+str(a.size())+'\n')
    print("Testing search: a.search(item)")
    print('Search 30: '+str(a.search(30)))
    print('Search "Guo": '+str(a.search('Guo')))
    print('Search "Hanbo": '+str(a.search("Hanbo"))+'\n')
    print("Testing remove: a.remove(item)"+'\n')
    a.remove(40),a.remove(30)
    print(a)
    print('\n'+"Testing append: a.append(item)")
    a.append('Guo')
    for i in range(0,40,4):
        a.append(i)
    print(a)
    print('\n'+"Testing index: a.index(item)")
    print('Index "Hanbo": '+str(a.index('Hanbo')))
    print('Index 28: '+str(a.index(28))+'\n')
    print("Testing insert: a.insert(pos,item)")
    a.insert(0,"Very"),a.insert(1,"Handsome"),a.insert(-1,"End"),a.insert(-2,"Another End")
    print(a)
    print('\n'+"Testing pop: a.pop(pos)")
    print("pop(0): "+str(a.pop(0)))
    print("pop(): "+str(a.pop()))
    print("pop(7): "+str(a.pop(7))+'n')
    print(a)
    print('\n'+"All done!")

