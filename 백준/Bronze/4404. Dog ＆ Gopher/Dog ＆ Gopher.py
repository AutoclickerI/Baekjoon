a,b,c,d=map(float,input().split())
e=input()
while e:
    f,g=map(float,e.split())
    if 4*(a-f)**2+4*(b-g)**2<=(c-f)**2+(d-g)**2:break
    try:e=input()
    except:e=0
print(f'The gopher can escape through the hole at ({",".join(e.split())}).'if e else'The gopher cannot escape.')