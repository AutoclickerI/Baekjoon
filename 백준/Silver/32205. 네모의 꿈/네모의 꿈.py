s={a:=0}
for i in[*open(0)][1:]:x={*i.split()};a|=bool(x&s);s|=x
print(a)