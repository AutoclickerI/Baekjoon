p=''
while(s:=input())<'9'*5:
 if i:=sum(map(int,s[:2])):p='rliegfhtt'[i%2::2]
 print(p,s[2:])