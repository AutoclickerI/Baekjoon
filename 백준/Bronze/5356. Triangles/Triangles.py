l=[]
for i in[*open(0)][1:]:a,b=i.split();l+=[-~i*chr(65+(ord(b)-65+i)%26)for i in range(int(a))]+['']
print(*l,sep='\n')