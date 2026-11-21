N=int(input())
s=input()
ans=[]
scount=ncount=0
for i in s[::-1]:
    if i=='S':
        if scount:
            scount-=1
            ans+='N',
        else:
            ans+='U','N'
            ncount+=1
    if i=='U':
        if ncount:
            ncount-=1
            ans+='N',
        else:
            ans+='S','N'
            scount+=1
print(len(ans))
print(''.join(ans))