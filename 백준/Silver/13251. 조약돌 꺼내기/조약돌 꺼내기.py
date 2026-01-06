M,*c,K=map(int,open(0).read().split())
from math import*
print(sum(map(comb,c,[K]*99))/comb(sum(c),K))