N,U,L=map(int,input().split())
print(['Bad','Very '*(U>7999or L>259)+'Good'][N>999])