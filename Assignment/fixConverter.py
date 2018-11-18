import re
import math
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

class queue:
    '''Initialize queue object
    queue: last in first out'''
    def __init__(self):
        self.result=[]
    def enqueue(self,item):
        '''queue.enqueue(item) -> None -- add new item to the rear'''
        self.result.append(item)
    def dequeue(self):
        '''queue.dequeue() -> None -- remove the front object'''
        try:
            return self.result.pop(0)
        except Exception:
            return 'Empty queue'
    def isEmpty(self):
        '''queue.isEmpty() -> boolean -- see if the queue is empty'''
        return not self.result
    def size(self):
        '''queue.size() -> integer -- number of items'''
        return len(self.result)
    def getQueue(self):
        return self.result
    def __str__(self):
        return str(self.result)

def In_to_post(expression):
    '''In_to_post(expression) -> str -- convert infix to postfix'''
    q=queue()
    ex=expression.split(' ')
    index=-5
    for i in range(len(ex)):
        if ex[i]=='(':
            index=i+1
            temp=''
            while ex[index]!=')':
                temp+=ex[index]
                index+=1
            q.enqueue(temp)
        elif ex[i]==')':
            try:
                q.enqueue(ex[i+1])
            except Exception:
                pass
        elif ex[i] in '0123456789ABCDEFGHIJKLMN+-*/' and i>index+1:
            q.enqueue(ex[i])
    output=[]
    while has_letter(q.getQueue()):
        first=q.dequeue()
        if len(first)>=3:
            first=first[0]+first[-1]+first[-2]
            output.append(first)
        elif first in ['*','/','**']:
            second=q.dequeue()
            try:
                second=second[0]+second[-1]+second[-2]
            except Exception:
                a=0
            output.append(second+first)
        elif first in '+-':
            q.enqueue(first)
        else:
            output.append(first)
    while not q.isEmpty():
        output.append(q.dequeue())
    return ''.join(output)

def has_letter(obj):
    dig='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in obj:
        if i in dig:
            return True
        elif len(i)>1:
            for j in i:
                if j in dig:
                    return True
    return False

def eval_post(expression):
    '''eval_post(expression) -> number -- calculate post fix expression'''
    s=stack()
    try:
        expression=re.compile('\^').sub('**',expression)
    except Exception:
        pass
    ex=expression.split(' ')
    for i in ex:
        try:# bug: float?
            i=int(i)
            s.push(i)
        except ValueError:
            if len(i)==3:
                num=s.pop()
                s.push(eval('math.'+i+'('+str(num)+')'))
            else:
                first,second=str(s.pop()),str(s.pop())
                s.push(eval(second+i+first))
    return s.pop()

def Post_to_in(expression): # Still with ()
    '''Post_to_in(expression) -> str -- convert postfix to infix'''
    s=stack()
    expression=re.compile('\^').sub('**',expression)
    ex=expression.split(' ')
    for i in ex:
        if i in ['tan','sin','cos','cot','sec','csc']:
            first=s.pop()
            s.push(i+'('+first+')')
        elif i not in '+-*/':
            s.push(i)
        else:
            first=s.pop()
            second=s.pop()
            s.push('('+second+i+first+')')
    print(s)             


            
