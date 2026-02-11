for i in open(0):
    s,e=map(int,i.split())
    print(sum(len(str(i))==len({*str(i)})for i in range(s,e+1)))