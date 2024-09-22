R=range(N:=int(input()))
for i in R:print(''.join(chr(min(abs(i-j),abs(N+~i-j))%26+97)for j in R))