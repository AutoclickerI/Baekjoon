v=0
c=1
for i in[*open(0)][1].split():
    if int(i)==c:c+=1
    else:v+=1
print(v)