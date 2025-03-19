N,M=map(int,input().split())

s={*map(int,input().split()[1:])}

p=[{*map(int,input().split()[1:])}for _ in[0]*M]

v={*range(1,N+1)}

for _ in p:
    for i in p:
        if s&i:
            s|=i

v-=s

print(sum(i==v&i for i in p))