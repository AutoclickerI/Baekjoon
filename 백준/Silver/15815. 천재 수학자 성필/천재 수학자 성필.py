s=input()
st=[]
for i in s:
    if i in'+-*/':
        p1,p2=st[-2:]
        if i=='/':i*=2
        del st[-2:]
        st+=eval(f'{p1}{i}{p2}'),
    else:
        st+=i
print(*st)