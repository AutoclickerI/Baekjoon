s,t=input().split()
u=''.join({*t})
print(f'{int(s)+1906}{u}{len(t)-len(u)+4}_cpums'[::-1])