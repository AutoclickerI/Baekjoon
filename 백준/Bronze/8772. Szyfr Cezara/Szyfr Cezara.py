*l,=open(0,'rb')
for[*i,_],[j,_]in zip(l[2::3],l[3::3]):print(''.join(chr((j-i[0]+k+7)%26+97)for k in i))