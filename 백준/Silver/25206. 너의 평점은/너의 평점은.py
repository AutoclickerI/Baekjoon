a=s=0
d={'A+': 4.5,
 'A0': 4.0,
 'B+': 3.5,
 'B0': 3.0,
 'C+': 2.5,
 'C0': 2.0,
 'D+': 1.5,
 'D0': 1.0,
 'F': 0.0}
for i in open(0):
    p,q,r=i.split()
    if r=='P':continue
    a+=float(q)
    s+=d[r]*float(q)
print(f'{s/a:.6f}')