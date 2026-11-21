f=lambda:sorted(map(int,input().split()))
exec("l,_=f();print('YNEOS'[sum(f()[:l])<=sum(f()[-l:])::2]);"*f()[0])