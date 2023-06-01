I=input
exec('''n=len(s:=I().split()[1]*2);i=a=0
while i<n/2:
 a=k=i;j=i+1
 while j<n and s[k]<=s[j]:k=i if s[k]<s[j]else 1+k;j+=1
 while i<=k:i+=j-k
print(a);'''*int(I()))