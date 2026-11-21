b=[20*['.']for _ in[0]*10]
for i in[*open(0)][1:]:
    b[ord(i[0])-65][int(i[1:])-1]='o'
for i in b:print(''.join(i))