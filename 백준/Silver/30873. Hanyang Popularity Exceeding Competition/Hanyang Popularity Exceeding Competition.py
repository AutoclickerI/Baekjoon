for i in[*open(c:=0)][1:]:P,C=map(int,i.split());c+=abs(c-P)<=C
print(c)