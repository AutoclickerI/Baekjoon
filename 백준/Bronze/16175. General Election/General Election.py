I=input
for _ in[0]*int(I()):N,M=map(int,I().split());*l,=map(sum,zip(*[map(int,I().split())for _ in[0]*M]));print(l.index(max(l))+1)