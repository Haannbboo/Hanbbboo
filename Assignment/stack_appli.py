'''
@Haannbboo
Created at Nov.13th
:stack practice hw
'''

from pythonds.basic.stack import Stack
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
