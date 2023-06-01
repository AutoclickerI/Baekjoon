p,q,*l=map(int,open(0).read().split())
t=[1,1<<32]
while t[1]-t[0]-1:m=sum(t)//2;t[sum(i//m for i in l)<q]=m
print(t[0])    