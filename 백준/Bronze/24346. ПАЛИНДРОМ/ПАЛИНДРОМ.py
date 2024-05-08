s=input()
print(max(1,sum(s.count(i)&1for i in{*s})))