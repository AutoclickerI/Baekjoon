for _ in[0]*int(input()):print(*[(sum(i)+5)//10for i in zip(*[map(int,input().split())for _ in[0]*10])])