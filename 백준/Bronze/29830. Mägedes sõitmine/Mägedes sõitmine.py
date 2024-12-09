input()
s,*l=map(int,input().split())
for v,d in zip(l,map(int,input().split())):s+=d;print(end='MVT'[(v<s)-(v>s)])