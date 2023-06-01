exec('''n=len(s:=input()*2);i=a=0
while i<n/2:
 a=k=j=i
 while(j:=j+1)<n and s[k]<=s[j]:k=i if s[k]<s[j]else 1+k
 while i<=k:i+=j-k
print(a+1);'''*int(input()))