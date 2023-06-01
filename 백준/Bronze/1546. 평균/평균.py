a = input()
b = list(map(int, input().split(' ')))
b.sort()
print((100*sum(b))/(len(b)*b[-1]))