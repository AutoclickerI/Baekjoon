I=lambda:input().split()
while s:=I()[1:]:l={*I()};f=0;exec('_,r,*x=I();f|=int(r)>len(l&{*x});'*int(*s));print('yneos'[f::2])