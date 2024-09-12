l=sorted(map(int,[*open(0)][1].split()))
print(min(map(sum,zip(l,l[::-1]))))