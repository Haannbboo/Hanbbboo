'''
@Haannbboo
Created at Nov.11, 2018
'''

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



