k=int(input().split()[0])
print(*map(lambda i:[i,chr((t:=65+32*('`'<i))+(ord(i)+k-t)%26)][i.isalpha()],input()),sep='')