a,b=open(0)
k='false ','true '
n='null\n'
print([k[a==b]+k[a.lower()==b.lower()*(b!=n)],'NullPointerException '*2][a==n])