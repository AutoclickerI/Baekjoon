n=int(input())
b=[]
for i in input():b+=' '*i.isalpha()or i
l=[*map(int,''.join(b).split())]
print(*map(n.__mul__,l)if l else['N/A'])