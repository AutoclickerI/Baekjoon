a,b,c=map(int,input().split())
a+=b
print('%d'%max(c*c-a,a**.5))