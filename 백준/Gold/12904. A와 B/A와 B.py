s=input()
t=input()
print(+any(s==(t:=t[:-1][::-(t[-1]>'A')|1])for _ in t))