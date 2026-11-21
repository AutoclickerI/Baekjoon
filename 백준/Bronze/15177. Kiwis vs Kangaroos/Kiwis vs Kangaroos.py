*l,=map(input().lower().count,'aagnoobdiiiw')
f=sum(l)-sum(l[:6])*2
print(['Feud continues','Kiwis','Kangaroos'][(0<f)-(0>f)])