s=[0,0]
t=[0,0]
w=0
for c in input():
    if c=='R':w^=1
    if c!='Q':
        if max(t)==2:continue
        s[w]+=1
        if s[w]>max(4,s[1-w]+1) or s[w]>9:t[w]+=1;s=[0,0]
    elif max(t)<2:print(f"{t[0]} ({s[0]}{('*','')[w]}) - {t[1]} ({s[1]}{('','*')[w]})")
    else: print(f"{t[0]} {('','(winner) ')[t[0]>1]}- {t[1]}{('',' (winner)')[t[1]>1]}")