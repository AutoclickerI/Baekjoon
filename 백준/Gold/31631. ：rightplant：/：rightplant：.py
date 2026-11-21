n,i,*l=int(input()),0
while i<n:i+=1;l[:(n+~i&2)*n]+=i,
print(*l)