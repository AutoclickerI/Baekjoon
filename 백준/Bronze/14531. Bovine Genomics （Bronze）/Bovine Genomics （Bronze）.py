N=int(input().split()[0])
f=lambda:zip(*eval('input(),'*N))
print(sum({*x}&{*y}<{0}for x,y in zip(f(),f())))