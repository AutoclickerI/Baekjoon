_,*l=map(int,open(0).read().split())
print(max(min(l[1::4])-max(l[::4]),0)*max(min(l[3::4])-max(l[2::4]),0))