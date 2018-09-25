def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def generate_file():
    '''
    No input parameter
    Returns a generated file to your computer, for later use
    '''
    f=open('generation.txt','w')
    for i in range(20):
        f.write("The {}th term in fib is: {} \n".format(i+1,fib(i)))
    f.close()

def reverse_file():
    '''
    No input parameter
    Returns a file with lines of 'generate_file()' in reversed order
    '''
    g=open('reverse.txt','w')
    f=open('generation.txt','r')
    a=f.readlines()
    for i in range(len(a)-1,0,-1):
        new=a[i]
        g.write(str(new))
    g.close()

def snake_file():
    '''
    No input parameter
    Returns a file with lines of generate_file() which contain the string 'snake'
    '''
    h=open('snake.txt','w')
    f=open('generation.txt','r')
    a=f.readlines()
    for line in a:
        if 'snake' in line:
            print(line)
    h.close()

def num_file():
    '''
    No input parameter
    Returns a file with first five colums of reverse_file() replaced by ordered number
    '''
    x=open('addnum.txt','w')
    f=open('reverse.txt','r')
    cnt=1001
    for line in f:
        x.write(str(cnt)+' '+line)
        cnt+=1
    x.close()
    x=open('addnum.txt','r')
    return x.readlines()

def renum_file():
    '''
    No input parameter
    Returns a file that undoes the process of num_file()
    '''
    y=open('readdnum.txt','w')
    f=open('addnum.txt','r')
    for line in f:
        y.write(line[5:])
    y.close()
    
