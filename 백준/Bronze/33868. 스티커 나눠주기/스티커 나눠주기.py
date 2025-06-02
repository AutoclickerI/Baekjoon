T,B=zip(*[map(int,i.split())for i in open(0)][1:])
print(max(T)*min(B)%7+1)