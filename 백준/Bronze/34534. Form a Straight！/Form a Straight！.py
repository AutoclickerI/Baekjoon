x={*input()}
print(min(len({*'123456789'[i:i+5]}-x)for i in range(5)))