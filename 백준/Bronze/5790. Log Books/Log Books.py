while N:=int(input()):
 d=n=f=0;l=eval('[*map(lambda i:int(i[:2])*60+int(i[3:]),input().split())],'*N)
 for p,q,s,e in l:v=e-s;f|=v>120;d+=v;n+=[v,x:=max(0,p-s)+max(0,e-q)][2*x<v]
 print('PNAOSNS'[f|(d<3000)|(n<600)::2])