t=10
f={'A':11}
for c in"KQJT":f[c]=t
for i in range(t):f[str(i)]=i
while n:=int(input()):a,b,c=map(f.get,input().split());v=b+c-a-t*(b+c>21);e=a>t;d=2-e;e*=t;print(f"{((min(max(0,v-d),t)+(v>t)*3)*4*n-(a-e<v)-(b-e*(b>t)<v)-(c-e*(c>t)<v))*100/(52*n-3):.3f}%")