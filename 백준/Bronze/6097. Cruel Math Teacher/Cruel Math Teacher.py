a,b=map(int,input().split());n=str(a**b)
p=0
while p<len(n):
    print(n[p:p+70])
    p+=70