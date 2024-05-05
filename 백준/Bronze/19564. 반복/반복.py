s=input()
print(1+sum(x>=y for x,y in zip(s,s[1:])))