n=int(''.join(sorted(input())[::-1]))
print(-(n%30>0)or n)