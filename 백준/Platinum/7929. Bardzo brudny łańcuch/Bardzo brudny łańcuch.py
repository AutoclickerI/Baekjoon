exec('''n=len(s:=input());s+=s;i=a=0
while i<n:
 a=k=j=i
 while s[k]<=s[(j:=j+1):j+1]:k=[k+1,i][s[k]<s[j]]
 while i<=k:i+=j-k
print(s[a:a+n]);'''*int(input()))