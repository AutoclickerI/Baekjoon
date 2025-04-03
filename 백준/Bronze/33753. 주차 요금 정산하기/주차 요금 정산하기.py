A,B,C,T=map(int,open(0).read().split())
if T<31:
    print(A)
else:
    print(A-(T-30)//-B*C)