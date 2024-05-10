p=1-eval(input())
print(min(range(2,17),key=lambda N:(1/N-1)*p**N))