a,b,c,d,e=[int(input())for i in range(5)]
print(min(e*a,(e-c)*d+b)if e>c else min(e*a,b))