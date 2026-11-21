while(l:=input())>'.':
 m=j=i=0;f=[0];N=len(l)
 while(j:=j+1)<N:
  if l[i]==l[j]:f+=[f[-1]+1];i+=1
  else:f+=[0];i=0;j-=(l[i]==l[j])
  m=max(m,f[-1])
 print(1if-m+f[-1]-N%(N-m)else N//(N-m))