x=c=0
e=-30
for _ in[0]*int(input()):
    p,q=input().split()
    if p[1]=='e':e+=int(q)
    if p[1]=='x':x+=int(q)
    if p[1]=='c':c+=int(q)
print((1-(x>13>8<c>7<e))*'not '+'liveable')