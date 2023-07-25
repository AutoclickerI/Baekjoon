p=''
while(s:=input())<'9'*5:
 if i:=int(s[:2]):p='rliegfhtt'[(i//10^i)&1::2]
 print(p,s[2:])