'''

@Haannbboo
Created at Nov.14th
:parChecker and converter

'''
import unittest
class stack:
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
    
def parChecker(string):
    '''parChecker(string) -> boolean -- see if parenthesis is paired'''
    s=stack()
    dic={'(':')','[':']','{':'}'}
    for i in string:
        if i in '([{':
            s.push(i)
        else:
            if s.isEmpty():
                return False
            elif dic[s.peek()]!=i:
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False
    
'''
def binDec(integer):
    #binDec(integer) -> bin -- convert denary to binary
    s=stack()
    while integer!=0:
        s.push(integer%2)
        integer//=2
    result=''
    while not s.isEmpty():
        result+=str(s.pop())
    return int(result)
'''

def converter(number,decimal,base):
    '''converter(number,decimal,base) -> number -- convert decimal number to base number
    :number -> integer
    :decimal -> base for the number
    :base -> convert to base
    '''
    digit='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    s=stack()
    integer=int(str(number),decimal)
    while integer!=0:
        s.push(digit[integer%base])
        integer//=base
    result=''
    while not s.isEmpty():
        result+=str(s.pop())
    return result

class test(unittest.TestCase):
    def test_parChecker(self):
        self.assertTrue(parChecker('(({}[]{({}[])})[])'))
        self.assertFalse(parChecker('(({[]}[))'))
    def test_converter(self):
        self.assertEqual(converter(117,10,2),str(1110101))
        self.assertEqual(converter(117,8,2),str(1001111))

if __name__=='__main__':
    unittest.main()
