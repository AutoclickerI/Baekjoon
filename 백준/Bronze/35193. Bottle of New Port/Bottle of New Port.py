d,a,o,da,do=map(int,open(0).read().split())
aa=max(0,a-d*da)
oo=max(0,o-d*do)
print(aa/(aa+oo)*100)