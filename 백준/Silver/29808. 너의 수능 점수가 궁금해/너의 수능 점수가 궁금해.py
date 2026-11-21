n=int(input())
if n%4763:
    print(0)
else:
    ans=[]
    n//=4763
    for i in range(201):
        for j in range(201):
            if n in[508*i+212*j,108*i+212*j,508*i+305*j,108*i+305*j]:
                ans+=[i,j],
    print(len(ans))
    for i in ans:print(*i)