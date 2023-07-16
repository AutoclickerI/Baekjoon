while n:=int(input()):
    L=[[*map(int,input().split())]for _ in[0]*n]
    I,J=L[n//2]
    print(sum(k>I and l>J or k<I and l<J for k,l in L),sum(k>I and l<J or k<I and l>J for k,l in L))