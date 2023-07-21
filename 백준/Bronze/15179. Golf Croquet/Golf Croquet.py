team1name=input()
team2name=input()
input()
c=0
t=[0,0]
for i in input():
    if i=='H':
        t[c]=min(7,t[c]+1)
    if i=='D':
        t[c]=min(7,t[c]+2)
    if i=='O':
        t[~-c]=min(7,t[~-c]+1)
    c^=1
    if 7 in t:break
print(team1name,t[0],team2name,str(t[1])+'.',end=' ')
if t[0]==7:
    print(team1name,'has won.')
elif t[1]==7:
    print(team2name,'has won.')
elif t[0]==t[1]:
    print('All square.')
elif t[0]>t[1]:
    print(team1name,'is winning.')
else:
    print(team2name,'is winning.')