[N],P,S=[[*map(int,i.split())]for i in open(0)]
T=N//3*[0,1,2]
r=0
while T!=P:
    r+=1
    T=[T[i]for i in S]
    if T==N//3*[0,1,2]:
        print(-1)
        break
else:
    print(r)