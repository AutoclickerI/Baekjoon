def solution(N, tops):
    mod=10007
    no=1
    o=0
    for i in range(1,N*2+1):
        if i%2:
            if tops[i//2]:
                o,no=no*2+o,o+no
            else:
                o,no=no,o+no
        else:
            o,no=no,(o+no)%mod

    return (o+no)%mod