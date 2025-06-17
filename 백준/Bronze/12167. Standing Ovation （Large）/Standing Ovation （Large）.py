for x in open(T:=0).read().split()[2::2]:
 s=a=0;T+=1
 for v in x:m=max(s,0);a+=m;s-=m+int(v)-1
 print(f'Case #{T}:',a)