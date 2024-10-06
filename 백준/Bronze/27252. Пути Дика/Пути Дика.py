s=input()
l=[len(s)*['.']for _ in[0]*100]
w=99
h=0
for i in s:
    if i=='(':
        l[w][h]='/'
        w-=1
    else:
        w+=1
        l[w][h]='\\'
    h+=1
for i in l:
    if{*i}-{'.'}:print(*i,sep='')