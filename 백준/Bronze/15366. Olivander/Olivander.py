f=lambda:sorted(map(int,input().split()))
f()
print('DNAE'[any(x>y for x,y in zip(f(),f()))::2])