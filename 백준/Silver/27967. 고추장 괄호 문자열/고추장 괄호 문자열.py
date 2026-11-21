n,s=open(0)
print(s.replace(*'G(',int(n)//2-s.count('(')).replace(*'G)'))