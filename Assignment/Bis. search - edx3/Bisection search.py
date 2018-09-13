num=int(input("Type in a number: "))
x=abs(num)
epsilon =0.01
count=0
low=0.0
high=max(1.0,x)
a=(high+low)/2.0
while abs(a**3-x)>=epsilon:
    print("Low =", low, "high =", high, "ans =", a)
    count+=0
    if a**3<x:
        low=a
    else:
        high=a
    a=(high+low)/2.0
print("Guesses: ",count)
if num<0:
    a=-a
else:
    a=a
print(a, "is close to cube root of x")
