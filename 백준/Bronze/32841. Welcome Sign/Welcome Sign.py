_,c,*l=open(f:=0).read().split()
for s in l:x=int(c)-len(s);v=x+f>>1;print('.'*v+s+'.'*(x-v));f^=x%2