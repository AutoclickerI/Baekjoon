while(l:=input())>'.':
 m=j=i=0;f=[0];N=len(l)
 while(j:=j+1)<N:
  if l[i]==l[j]:f+=[f[-1]+1];i+=1
  else:f+=[0];i=0;j-=(l[i]==l[j])
  m=max(m,f[-1])
 if m-f[-1]or N%(N-m):print(1)
 else:print(N//(N-m))