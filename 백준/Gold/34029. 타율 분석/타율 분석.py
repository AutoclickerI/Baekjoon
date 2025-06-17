import math
A,B=map(int,input()[2:].split())
t=5*10**(3*B-2)
a=i=0
while 1:a+=A**i*(1000-A)**(B-i)*math.comb(B,i);t<=a<exit(print(i));i+=1