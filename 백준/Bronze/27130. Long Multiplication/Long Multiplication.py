n=int(input())
s=input()
print(n)
print(s)
for i in s[::-1]:
    print(int(i)*n)
print(int(s)*n)