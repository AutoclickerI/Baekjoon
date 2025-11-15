from itertools import*
for i in[*open(0)][1:]:
    n=int(i)
    l=['']*(2*n-1)
    l[::2]=map(str,range(1,n+1))
    ans=[]
    for i in product(['+','-',' '],repeat=n-1):
        l[1::2]=i
        if eval(''.join(l).replace(' ','_'))==0:ans+=''.join(l),
    ans.sort()
    for i in ans:print(i.replace('_',' '))
    print(end='\n')