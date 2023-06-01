l=sorted(map(int,input().split()))
p,q,r=map(int,input().split())
if sum(l)*(1-p/100)<l[0]+l[1]*(1-min(q,r)/100)+l[2]*(1-max(q,r)/100):
    print(f'one {sum(l)*p/100:.2f}')
else:
    print(f'two {l[1]*min(q,r)/100+l[2]*max(q,r)/100:.2f}')