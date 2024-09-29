for i in[*open(0)][1:]:
 c=0;n=int(i)
 while 9<n:n=str(n);n=max(int(n[:i])*int(n[i:])for i in range(1,len(n)));c+=1
 print(c)