from itertools import*
while'#'<(s:=input()):s=[f'{v} {v} glued'for v,w in groupby(s.split()[1])if len([*w])>1];s and print(*s,sep=' and ')