for i in[*open(T:=0)][1:]:
    T+=1;R,C=map(int,i.split());print(f'Case #{T}: ..+'+'-+'*~-C+' .'+'.|'*C+' +'+'-+'*C)
    for _ in[0]*~-R:print('|'+'.|'*C+' +'+'-+'*C)