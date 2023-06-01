*l,=map(int,open(0).read().split())
e=0
print(sum((e:=i)and 1for i,j in sorted(zip(l[2::2],l[1::2]))if e<=j))