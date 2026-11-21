N,M=map(int,input().split())
for _,c in sorted(sorted(enumerate(input()),key=lambda s:s[1])[M:]):print(end=c)