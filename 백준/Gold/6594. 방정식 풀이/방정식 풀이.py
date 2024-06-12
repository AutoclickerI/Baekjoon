x=1j
for j in open(i:=0):i+=1;p,q=map(eval,j.split('='));p-=q;p,q=p.real,-p.imag;print(f"Equation #{i}\n{['No solution.','Infinitely many solutions.'][p==0]if q==0else f'x = {p/q:.6f}'}\n")