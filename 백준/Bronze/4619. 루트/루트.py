for i in[*open(0)][:-1]:
    a,b=map(int,i.split())
    i=1
    p=a
    while p>(p:=abs(a-i**b)):i+=1
    print(i-1)