
a=int(input("Type in a number： "))

def for_mt():
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("{}*{}= {}".format(i,j,i*j), end=" ")
        print(" ")

def while_mt():
    x,y=1,0
    while x<=a:
        while y<x:
            y+=1
            print("{}*{} = {}".format(x,y,x*y), end=" ")
        y=0           
        x+=1
        print(" ")
        
