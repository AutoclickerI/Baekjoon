k='ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()
while'#'<(s:=input()):i=0;print(''.join((a:=[t for t in(*k,*map(str.lower,k))if j in t][0])[(a.find(j)-(i:=i+1))%len(a)]for j in s))