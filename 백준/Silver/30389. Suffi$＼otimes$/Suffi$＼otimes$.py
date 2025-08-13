s=set()
for i in[*open(0)][1:]:s^={i[j:]for j in range(len(i)-1)}
print(len(s))