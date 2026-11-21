E1=E2=V1=V2=0
for _ in[0]*int(input()):
    e,v1,v2=map(int,input().split())
    V1+=v1
    V2+=v2
    if v1>v2:E1+=e
    if v2>v1:E2+=e
if V1>V2 and E1>E2:print(1)
elif V1<V2 and E1<E2:print(2)
else:print(0)