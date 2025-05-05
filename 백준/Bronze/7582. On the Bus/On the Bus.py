I=input
while'$'<(s:=I()):v,w=s.split();w=int(w);p=int(I());exec('p=min(w,p-eval(I().replace(*" -")));'*int(I()));print(v,p)