from statistics import*
print(*multimode(''.join(sorted(open(0).read())).strip()),sep='')