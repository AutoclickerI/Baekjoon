s={*input().split()[1:]}
t=int(input())
print(min(abs(i-t)for i in range(1000)if~-any(s&{*str(i)})))