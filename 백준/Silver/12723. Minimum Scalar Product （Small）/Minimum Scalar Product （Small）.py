f=lambda:sorted(map(int,input().split()))
exec("i+=1;f();print(f'Case #{i}:',sum(x*y for x,y in zip(f(),f()[::-1])));"*f()[i:=0])