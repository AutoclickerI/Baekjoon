*l,=map(input().lower().count,'aagknoorbdiiikrw')
A=sum(l[:8])
B=sum(l)-A
print(['Feud continues','Kiwis','Kangaroos'][(A<B)-(A>B)])