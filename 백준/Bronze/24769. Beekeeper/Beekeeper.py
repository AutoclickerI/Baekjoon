while s:=int(input()):print(max([input()for _ in[0]*s],key=lambda s:sum(map(s.count,['aa','ee','ii','oo','uu','yy']))))