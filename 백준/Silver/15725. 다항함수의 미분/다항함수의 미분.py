s=input()
a=s.split('x')[0]
print((a+'1'*(a=='-')or 1)*('x'in s)or 0)