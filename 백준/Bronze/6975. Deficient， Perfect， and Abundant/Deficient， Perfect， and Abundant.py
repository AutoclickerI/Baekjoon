f=lambda n:sum(i for i in range(1,n)if n%i==0)
for _ in[0]*int(input()):
    i=int(input())
    j=f(i)
    print(i,'is',['a perfect','an abundant','a deficient'][(i<j)-(i>j)],'number.\n')