f=lambda s:[int(i)for i in[(s+s)[j:j+len(s)]for j in range(len(s))]if'0'<i[0]]
print(max(f(input()))-min(f(input())))