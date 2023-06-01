l=[]
for _ in[0]*int(input()):
    p,*q=input().split()
    if p=='S':v=4/3*eval(q[0])**3
    else:v=eval(q[0])**2*eval(q[1])*(1-(p=='C')*2/3)
    l+=[v]
print(f'{max(l)*3.14159:.3f}')