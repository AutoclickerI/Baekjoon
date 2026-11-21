n=int(input())
t=1
h=0
while 2**t<n:
    t+=1
while 3**h<n:
    h+=1
print(sum(2**i*3**j<=n for i in range(1,t+1)for j in range(h+1)))