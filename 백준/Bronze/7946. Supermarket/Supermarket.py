f=lambda:[*map(int,input().split())]
exec('_,k=f();print(sorted(f())[k-1]);'*f()[0])