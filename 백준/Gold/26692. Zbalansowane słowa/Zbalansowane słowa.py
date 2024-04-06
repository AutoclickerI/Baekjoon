s=input()
l=[]
abc={(0,0):1}
a=b=c=prev=0
for i in s:
    if prev!=i:
        prev=i
        l+=[0,i],
    a+=i=='a'
    b+=i=='b'
    c+=i=='c'
    abc[a-b,b-c]=abc.get((a-b,b-c),0)+1
    l[-1][0]+=1

ans=sum(i*(i+1)//2 for i,_ in l)+sum(i*(i-1)//2 for i in abc.values())
if len(l)<2:
    exit(print(ans))

l2=[['a'*l[0][0],'b'*l[1][0]]]
prev=l[0][1]
t=0
for i in range(2,len(l)):
    if l[i][1]==prev:
        l2[-1]+=chr(97+t)*l[i][0],
        t^=1
    else:
        l2+=['a'*l[i-1][0],'b'*l[i][0]],
        t=0
    prev=l[i-1][1]

for s in[''.join(i)for i in l2]:
    ab={0:1}
    a=b=prev=0
    for i in s:
        a+=i=='a'
        b+=i=='b'
        ab[a-b]=ab.get(a-b,0)+1
    ans+=sum(i*(i-1)//2 for i in ab.values())
print(ans)