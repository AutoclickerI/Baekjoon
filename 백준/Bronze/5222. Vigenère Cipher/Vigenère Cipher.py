for i in[*open(0,'rb')][1:]:v,w=i.split();print('Ciphertext:',''.join(chr((i+j)%26+65)for i,j in zip(v*99,w)))