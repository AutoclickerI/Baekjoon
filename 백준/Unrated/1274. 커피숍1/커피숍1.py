from decimal import*
getcontext().prec=1000
a,b=map(D:=Decimal,input().split())
Sa,Sb,S=map(D,input().split())
before=ans=0
while S<=Sa and before<=a:
    before=a
    a=(a*(Sa-S)+b*S)/Sa
    ans+=1
    if S>Sb or ans>100:break
    b=b*(Sb-S)/Sb
print(hex(ans)[2:].upper()if 0<ans<51 else'gg')