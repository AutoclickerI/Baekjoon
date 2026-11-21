input()
s=input()
print(min(f(i).count(i)for i in'RB'for f in(s.rstrip,s.lstrip)))