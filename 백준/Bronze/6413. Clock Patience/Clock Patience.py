A=1
T=10
J=11
Q=12
K=13
while(S:=input())!='#':
    c=0
    s='K'
    l=[[*i]for i in zip(S.split(),input().split(),input().split(),input().split())][::-1]
    try:
        while 1:
            s=l[eval(s[:1])-1].pop(0)
            c+=1
    except:
        print(f'{c:02},{s}')