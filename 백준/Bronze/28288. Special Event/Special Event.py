m=max(l:=[i.count('Y')for i in zip(*open(0).read().split()[1:])])
print(*[i+1for i in range(5) if l[i]==m],sep=',')