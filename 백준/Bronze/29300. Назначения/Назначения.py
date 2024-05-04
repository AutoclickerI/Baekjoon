s=input()
print(min(s.replace(i,'')for i in{*s}))