n,_,*l=open(0).read().split()
n=int(n)
i=0
if len(l)>9:exit(print(abs(n-100)))
while 1:
    if{*l}&{*str(abs(n-i))}and{*l}&{*str(n+i)}:i+=1;continue
    print(min(len([str(n+i),str(abs(n-i))][{*l}&{*str(abs(n-i))}==set()])+i,abs(n-100)))
    break