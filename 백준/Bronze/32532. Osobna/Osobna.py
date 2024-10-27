a,b,c=open(0)
z=c.split('<')
print(f'''Ime: {z[0].title()}
Prezime: {z[2].title()}
Datum rodjenja: {b[4:6]}-{b[2:4]}-{'20'if int(b[:2])<25 else'19'}{b[:2]}
OIB: {a[15:26]}''')