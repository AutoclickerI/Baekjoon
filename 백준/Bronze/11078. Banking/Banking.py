ptr=0
p=input()
a=''
for i in input():
    if i.isupper():
        ptr+=ord(i)-64
    else:
        skip=ord(i)-96
        a+=p[ptr:ptr+skip]
        ptr+=skip
if ptr==len(p):
    print(sum(map(int,a)))
else:
    print('non sequitur')