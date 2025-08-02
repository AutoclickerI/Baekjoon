N=[eval(i.replace(*' -'))for i in open(0)]
for i in range(1,4):print(-sum(N[i:]))