while'#'<(s:=input()):
 f=1
 for v in{i for i,j in zip(s,s[1:])if i==j}:print(*['and',v,v,'glued'][f:]);f=0