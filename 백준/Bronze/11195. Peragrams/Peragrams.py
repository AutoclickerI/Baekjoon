s=input()
print(max(0,sum(s.count(i)%2for i in{*s})-1))