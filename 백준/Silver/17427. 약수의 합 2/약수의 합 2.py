n=int(input())
print(sum(n-n%-~i for i in range(n)))