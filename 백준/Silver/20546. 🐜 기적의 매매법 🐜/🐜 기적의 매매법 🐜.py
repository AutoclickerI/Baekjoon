JH=SM=0
JHM=SMM=int(input())
pd=pu=0
*l,=map(int,input().split())
p=l[0]
for i in l:
    JH+=JHM//i
    JHM%=i
    if p<i:
        pu+=1
    else:
        pu=0
    if i<p:
        pd+=1
    else:
        pd=0
    if pd==3:
        SM+=SMM//i
        SMM%=i
    if pu==3:
        SMM+=SM*i
        SM=0
    p=i
JH=JHM+JH*i
SM=SMM+SM*i
if SM<JH:
    print('BNP')
elif JH<SM:
    print('TIMING')
else:
    print('SAMESAME')