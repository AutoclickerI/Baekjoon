N=int(input())
print(sum((N-4*i)%5<1for i in range(N//4+1)))