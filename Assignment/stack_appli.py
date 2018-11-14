'''
@Haannbboo
Created at Nov.13th
:stack practice hw
'''

#from pythonds.basic.stack import Stack
class Stack:
    '''Initialize stack object'''
    def __init__(self):
        self.result=[]
    def push(self,item):
        '''stack.push(object) -> None -- push item to the top'''
        self.result.append(item)
    def pop(self):
        '''stack.pop() -> item -- remove and return item at the top'''
        try:
            return self.result.pop()
        except IndexError:
            print(None)
            return
    def isEmpty(self):
        '''stack.isEmpty() -> boolean -- see whether the stack is empty'''
        return not self.result
    def peek(self):
        '''stack.peek() -> item -- get the top item'''
        if self.isEmpty():
            print(None)
            return
        else:
            return self.result[-1]
    def size(self):
        '''stack.size() -> integer -- return the number of item'''
        return len(self.result)
    def __str__(self):
        return str(self.result)
def parChecker(sample):
    '''parChecker(sampleString) -> boolean -- see if the parenthesis is paired'''
    s=Stack()
    for i in sample:
        if i=='(':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False

def revString(string):
    '''revString(string) -> string -- reverse the string'''
    s=Stack()
    for i in str(string):
        s.push(i)
    out=''
    while not s.isEmpty():
        out+=s.pop()
    return out
print('Test parChekcer')
print('True: '+str(parChecker('(()()())(()())((()))')))
print('False: '+str(parChecker('((()(())())')))
print('False: '+str(parChecker('(()))()))'))+'\n')
print('Test revString')
print(revString('Hanbo'))
print(revString(123))
