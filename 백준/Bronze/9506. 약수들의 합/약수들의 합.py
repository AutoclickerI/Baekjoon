while(n:=int(input()))!=-1:
    l=[i for i in range(1,n) if n%i==0]
    if sum(l)==n:print(n,'=',' + '.join(map(str,l)))
    else:print(n,'is NOT perfect.')