print(s:=input().lower())
for i in range(len(s)-1):
    if s[i:i+2]=='ss':print(s[:i]+'B'+s[i+2:])