r=[[],[]]
for i in range(2):
 for x,y in zip(input(),input()[::-1]):r[i]+=x+y,
 r[i].sort()
print('YNeos'[r[0]!=r[1]::2])