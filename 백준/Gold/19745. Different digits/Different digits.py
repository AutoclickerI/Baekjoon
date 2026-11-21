n=int(input())+1
*l,=map(int,str(n))
i=1
while i<len(l):
    if l[0]==10:
        exit(print(('10'*len(l))[:len(l)+1]))
    if l[i]==l[i-1]:
        l[i]+=1
        l[i+1:]=[0]*(len(l)-i-1)
    if l[i]==10:
        l[i]=0
        l[i-1]+=1
        i-=2
    i+=1
print(*l,sep='')