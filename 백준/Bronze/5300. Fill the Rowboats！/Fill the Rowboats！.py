l=[]
for i in range(int(input())):
    l+=[str(i+1)]
    if i%6==5:l+=['Go!']
l+=['Go!']*(l[-1]!='Go!')
print(' '.join(l))