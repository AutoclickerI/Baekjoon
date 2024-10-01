A=[[*map(int,i.split())]for i in open(0)]
print(min(range(4),key=[A[1][0],A[1][-1],A[-1][-1],A[-1][0]].__getitem__))