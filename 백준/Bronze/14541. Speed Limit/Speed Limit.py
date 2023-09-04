while~(n:=int(input())):
 a=p=0
 for _ in[0]*n:s,t=map(int,input().split());a-=s*(p-(p:=t))
 print(a,'miles')