for i in[*open(c:=0)][2::2]:
 a=i.split();n=len(a);s=0;c+=1
 for i in range(n):j=a.index(min(a[i:n],key=int));s+=j-i+1;a[i:j+1]=a[i:j+1][::-1]
 print(f"Case #{c}:",s-1)