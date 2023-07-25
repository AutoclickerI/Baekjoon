p=''
while(s:=input())<'9'*5:
 if i:=int(s[:2]):p='rliegfhtt'[(i+i//10)%2::2]
 print(p,s[2:])