import turtle as t
def draw(linelen):
    if linelen>0:
        t.forward(linelen)
        t.right(90)
        draw(linelen-5)

def mult_iter(a,b):
    '''
    a,b: two integers
    returns: the value of a times b
    '''
    result=0
    while b>0:
        result+=a
        b-=1
    return result

def sum_recur(n):
    '''
    n: an integer
    returns: the sum of 1+2+3+...+n
    '''
    if n==1:
        return 1
    else:
        return n+sum_recur(n-1)

def test_sum_recur():
    for n in (1,10,-5):
        print("Testing n = "+str(n))
        result=sum_recur(n)
        if result == None:
            print("No result")
        else:
            print("Sum result ="+str(result))
#test_sum_recur()
    

def factorial_recur(n):
    '''
    n: an integer
    returns: the factorial of n -> n!
    '''
    if n==1:
        return 1
    else:
        return n*factorial_recur(n-1)

def power_recur(a,b):
    '''
    a,b: two integers
    results: a times to the power of b, a**b
    '''
    if b==0:
        return 1
    else:
        return a*power_recur(a,b-1)

def n_fib(n):
    '''
    n: an integer
    returns: the nth term in the fibbonacci sequence
    '''
    if n==0 or n==1:
        return 1
    else:
        return n_fib(n-1)+n_fib(n-2)

def sum_fib(n):
    '''
    n: a positive integer
    returns: the sum of the first nth term of the fibbonacci sequence
    '''
    def n_fib(n):
        if n==0 or n==1:
            return 1
        else:
            return n_fib(n-1)+n_fib(n-2)
    if  n== 0:
        return 1
    else:
        return n_fib(n)+sum_fib(n-1)
'''
def n_fib_iter(n):
    a=0
    for i in range(1,n):
        
    return a

 '''   
