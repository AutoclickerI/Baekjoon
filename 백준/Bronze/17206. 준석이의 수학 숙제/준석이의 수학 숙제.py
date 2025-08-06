d=[i:=0]
while i<9e4:d+=d[i]+(i%3*i%7<1)*i,;i+=1
for n in[*open(0)][1].split():print(d[int(n)+1])