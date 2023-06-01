a=b=0
for i in[0]*int(input()):p,q=map(int,input().split());a,b=a+(p>q),b+(p<q)
print(a,b)