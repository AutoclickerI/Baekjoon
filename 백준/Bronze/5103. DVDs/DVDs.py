I=input
while'#'<(s:=I()):m,n=map(int,I().split());exec("o=I();n=max(0,min(m,n-int(o[1:])*(2*('S'<o)-1)));"*int(I()));print(s,n)