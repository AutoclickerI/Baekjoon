for i in range(1,len(s:=input())):
 if s[::-1]==s[i:]+s[:i]:print(s[:i],s[i:]);exit()
print('NO')