l,r,k=map(int,open(0))
if k==2:
    print(r-l+1-sum(l<=i<=r for i in(1,2)))
if k==3:
    print(r//3+l//-3+1-sum(l<=i<=r for i in(3,)))
if k==4:
    print(r//2+l//-2+1-sum(l<=i<=r for i in(2,4,6,8,12)))
if k==5:
    print(r//5+l//-5+1-sum(l<=i<=r for i in(5,10)))