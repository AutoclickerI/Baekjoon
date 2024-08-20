for i in[*open(0)][1:]:
 b=f'{int(i):b}';n=int(b[1:],2)+1
 for f in range(len(b),0,-1):print(f"{f}{n:018d}");n=-~n//2