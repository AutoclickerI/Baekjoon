t,m,o,x=open(0).read().replace(*': ').split()
t=int(t)%12*60+int(m)-int(x)-720*('P'<o)
t%=1440
print(f'{(t//60-1)%12+1}:{t%60:02d}','APMM'[719<t::2])