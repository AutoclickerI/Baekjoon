p=int(input())-1
q=210
for i in[0]*int(input()):
    a,b=input().split()
    q-=int(a)
    if q<=0:print(p+1);break
    if b=='T':p=(p+1)%8