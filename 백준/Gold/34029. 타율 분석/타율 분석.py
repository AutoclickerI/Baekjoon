import math
A,B=map(int,input()[2:].split())
a=i=0
while 1:a+=20*A**i*(1000-A)**(B-i)*math.comb(B,i);1000**B<=a<exit(print(i));i+=1