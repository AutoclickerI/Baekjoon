for i in[*open(T:=0)][1:]:T+=1;n,m,k=map(int,i.split());m+=k*(m%2*4-2)-1;print(f'Case #{T}:',-~m%n+1,~-m%n+1)