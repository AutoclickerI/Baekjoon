for x in open(T:=0).read().split()[2::2]:
 s=a=0;T+=1
 for i,v in enumerate(x):m=max(i-s,0);a+=m;s+=m+int(v)
 print(f'Case #{T}:',a)