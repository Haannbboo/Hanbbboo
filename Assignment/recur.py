import turtle as t
def draw(linelen):
    if linelen>0:
        t.forward(linelen)
        t.right(90)
        draw(linelen-5)

def mult_iter(a,b):
    result=0
    while b>0:
        result+=a
        b-=1
    return result

def sum_recur(n):
    if n==1:
        return 1
    else:
        return n+sum_recur(n-1)

def factorial_recur(n):
    if n==1:
        return 1
    else:
        return n*factorial_recur(n-1)

def power_recur(a,b):
    if b==0:
        return 1
    else:
        return a*power_recur(a,b-1)

def n_fib(n):
    if n==0 or n==1:
        return 1
    else:
        return n_fib(n-1)+n_fib(n-2)

def sum_fib(n):
    def n_fib(n):
        if n==0 or n==1:
            return 1
        else:
            return n_fib(n-1)+n_fib(n-2)
    if  n== 0:
        return 1
    else:
        return n_fib(n)+sum_fib(n-1)
    
