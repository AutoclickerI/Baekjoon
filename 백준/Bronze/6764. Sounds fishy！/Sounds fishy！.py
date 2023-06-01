a,b,c,d=[int(input())for i in range(4)]
print('Fish Rising'if a<b<c<d else'Fish Diving'if a>b>c>d else'Fish At Constant Depth'if a==b==c==d else'No Fish')