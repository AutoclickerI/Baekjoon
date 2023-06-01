n=int(input())
a=f=0
for i in map(int,input().split()):a^=i;f|=a
if f-1:print(['cubelover','koosaga'][a!=0])
else:print(['cubelover','koosaga'][a==0])