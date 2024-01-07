while(s:=input())>'1':
    N,M,P=map(int,s.split())
    s=sum(l:=[int(input())for _ in[0]*N])
    print(l[M-1]and s*(100-P)//l[M-1])