f=lambda x:x[-1]<'B'and f(x[:-1])or'B'<=x and f(x[:0:-1])if len(x)-len(S)else x==S
S=input()
print(+f(input()))