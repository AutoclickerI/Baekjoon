s=[0,0]
t=[0,0]
w=0
l=[]
for c in input():
    w^=c=='R'
    if c!='Q':
        if 1<max(t):continue
        s[w]+=1
        if min(9,max(4,s[w^1]+1))<s[w]:t[w]+=1;s=[0,0]
    elif max(t)<2:l+=t[0],f"({s[0]}{'*'[w:]}) - {t[1]} ({s[1]}{'*'[:w]})"
    else:l+=t[0],t[0]//2*'(winner) '+f"- {t[1]}"+t[1]//2*' (winner)'
print(*l)