s,t=open(0)
print(+any(s[:-1]==(t:=t[:-1][::-(t[-1]>'A')|1])for _ in t))