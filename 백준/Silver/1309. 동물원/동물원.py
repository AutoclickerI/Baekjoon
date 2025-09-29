a=b=1
for _ in[0]*int(input()):a,b=b,2*b+a
print(b%9901)