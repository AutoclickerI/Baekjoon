n=pow(*map(int,input().split()[1:]),26)
for i in input().split():print(*[chr((ord(j)+13-n)%26+65)for j in i],sep='')