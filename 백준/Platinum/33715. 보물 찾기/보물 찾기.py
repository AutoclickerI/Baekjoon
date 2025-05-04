def guess(x,y):
    print(x,y)
    n=int(input())
    if n<0:
        exit()
    return n

N=int(input())
d=set()

mode=0
line_e=N-1
for i in range(2,N):
    n=guess(i,i)
    if mode==0 and n in d:
        line_s=i-1
        mode=1
        prev=n
    if mode==1 and n!=prev:
        line_e=i-1
        break
    d.add(n)
    
guess(line_s,line_e)
guess(line_e,line_s)