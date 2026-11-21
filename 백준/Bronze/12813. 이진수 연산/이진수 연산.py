a,b=map(int,open(0),[8,8])
z=8**10**5//7
print((5*'%0100000o ')%(a&b,a|b,a^b,z-a,z-b))