s=input().encode()
for i in range(l:=len(s)//2):print(end=chr(65+sum(s+s[i::l])%26))