for i in[0]*int(input()):
 n=len(s:=input());s+=s;a=0
 while i<n:
  a=k=i;j=i+1
  while j<n*2and s[k]<=s[j]:k=i if s[k]<s[j]else 1+k;j+=1
  while i<=k:i+=j-k
 print(s[a:a+n])