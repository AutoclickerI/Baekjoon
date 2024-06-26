import sys
input=sys.stdin.readline
from datetime import*
today=datetime(*eval('2000+'+input().replace(*' ,')))   
for _ in[0]*int(input()):
    a,b,c=map(int,input().split())
    l=[]
    for i,j,k in[2000+a,b,c],[2000+c,a,b],[2000+c,b,a]:
        try:
            l+=datetime(i,j,k),
        except:0
    if l:
        s=(min(l)<today)*'un'+'safe'
    else:
        s='invalid'
    print(s)