for i in[*open(0)][1:]:
 Z,K=map(int,i.split());a=0
 while Z:a+=1;Z//=K+1
 print(a)