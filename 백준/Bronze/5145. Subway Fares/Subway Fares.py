I=input
for i in range(int(I())):c=[I()for _ in[0]*(2*int(I())-1)];f=c.index;print(f'Data Set {i+1}:\n{c[abs(f(I())-f(I()))-1]}\n')