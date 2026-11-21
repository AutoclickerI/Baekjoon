t=sum(s+m*60for m,s in(map(int,i.split(':'))for i in[*open(0)][1:]))
print(f"{t//3600:02}:{t//60%60:02}:{t%60:02}")