*l,=map(int,open(0).read().split())
s=lambda i:max(i)-min(i)
print(s(l[1::2])*s(l[2::2]))