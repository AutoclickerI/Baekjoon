s=input()
v='aeiou'
p=[i in v for i in s[::2]]
q=[i in v for i in s[1::2]]
print(+(all(p)and not any(q)or all(q)and not any(p)))