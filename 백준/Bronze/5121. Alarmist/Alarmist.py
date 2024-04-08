I=lambda:map(int,input().split())
for i in range(*I()):n,w=I();*l,=I();s=[sum(l[i:i+w])//w for i in range(n-w+1)];print(f'Data Set {i+1}:\n{max(s)-min(s)}\n')