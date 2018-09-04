# Question 1
def variable_print():
    A="All"
    w="work"
    a="and"
    n="no"
    p="play"
    m="makes"
    J="Jack"
    z="a"
    d="dull"
    b="boy"
    print(A,w,a,n,p,m,J,z,d,b)


# Question 2
def parenthesis():
    original=6 * 1 - 2
    parenthesis= 6 * ( 1 - 2)
    print("Original: {}, parenthesis: {}".format(original,parenthesis))

# Question 3
def comment():
    #Jibber Jabber 
    return print("#")

# Question 4
def error():
    try:
        bruce+4
    except NameError as e:
        print(e)
        bruce=6
    return bruce+4

# Question 5
def money():
    t=int(input("How many years: "))
    P=10000
    n=12
    r=0.08
    A=P*(1+r/n)**(n*t)
    return round(A,3)

# Question 6
def something_weird():
    5%2
    9%5
    15%12
    12%15
    6%6
    0%7
    try:
        7%0
    except ZeroDivisionError as e:
        print(e)

# Question 7
def alarm_clock():
    t=int(input("For how many hours: "))
    h=(14+t)%24
    d=(14+t)//24
    r="{}:00 +{}days".format(h,d)
    print(r)

# Question 8
def finally_done(n):
    n=int(input("The time now: "))
    t=int(input("For how many hours: "))
    h=(n+t)%24
    d=(n+t)//24
    r="{}:00 +{}days".format(h,d)
    print(r)
    
