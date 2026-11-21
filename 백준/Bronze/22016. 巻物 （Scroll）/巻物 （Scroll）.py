n,s=open(0)
z=int(n.split()[1])-1
print(s[:z]+s[z:].swapcase())