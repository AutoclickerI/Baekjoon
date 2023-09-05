m=[0,31,29,31,30,31,30,31,31,30,31,30,31]
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    if p<24 and q<60:print(end='Yes ')
    else:print(end='No ')
    if 0<p<13 and 0<q<=m[p]:print('Yes')
    else:print('No')