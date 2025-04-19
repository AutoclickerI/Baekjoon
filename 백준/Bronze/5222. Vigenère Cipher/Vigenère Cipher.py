n,*l=open(0,'rb')
for i in l:v,w=i.split();print('Ciphertext:',''.join(chr((i+j)%26+65)for i,j in zip(v*len(w),w)))