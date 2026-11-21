l=[*open(0)][1].split()
print(sum(abs(int(i)-int(j))for i in l for j in l))