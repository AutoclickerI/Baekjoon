exec('''n=len(s:=input()*2);i=a=0
while i<n/2:
 a=k=j=i
 while s[k]<=s[(j:=j+1):]:k=[k+1,i][s[k]<s[j]]
 while i<=k:i+=j-k
print(a+1);'''*int(input()))