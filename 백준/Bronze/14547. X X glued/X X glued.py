from itertools import*
while'#'<(s:=input()):print(end=''.join(f'{v} {v} glued and '*(len([*w])>1)for v,w in groupby(s))[:-4])