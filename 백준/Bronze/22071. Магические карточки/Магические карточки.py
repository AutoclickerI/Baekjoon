f=lambda:[*map(int,input().split())]
for _ in[0]*f()[0]:n,l=f();print('YNEOS'[sum(sorted(f())[:l])<=sum(sorted(f())[-l:])::2])