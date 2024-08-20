for i in[*open(0)][1:]:
 b=f'{int(i):b}';n=int(b[1:],2);f=len(b);
 while f:print(f'{f}{n+1:018}');n//=2;f-=1;