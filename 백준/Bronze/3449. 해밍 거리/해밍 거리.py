I=input
exec("print(f'Hamming distance is {sum(x!=y for x,y in zip(I(),I()))}.');"*int(I()))