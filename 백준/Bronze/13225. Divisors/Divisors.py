def div(n):
    n=int(n)
    ret=1
    for i in range(2,9999):
        cnt=1
        while n%i==0:
            n//=i
            cnt+=1
        ret*=cnt
    return ret
for i in map(int,[*open(0)][1:]):
    print(i,div(i))