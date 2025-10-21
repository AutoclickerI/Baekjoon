L,H=zip(*sorted([*map(int,i.split())]for i in[*open(0)][1:]))
m=H[0]
Hl=[m:=max(m,i)for i in H]
m=H[-1]
Hr=[m:=max(m,i)for i in H[::-1]][::-1]
*H,=map(min,Hl,Hr)
mi=H.index(max(H))
print(sum(i*(k-j)for i,j,k in[*zip(H[:mi],L,L[1:]),*zip(H[mi+1:],L[mi:],L[mi+1:])])+H[mi])