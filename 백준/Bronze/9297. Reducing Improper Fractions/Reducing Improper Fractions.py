for i in[*open(t:=0)][1:]:t+=1;a,b=map(int,i.split());print(f'Case {t}:',f'{a//b} '*(a//b>0)+f'{a%b}/{b}'*(a%b>0)or'0')