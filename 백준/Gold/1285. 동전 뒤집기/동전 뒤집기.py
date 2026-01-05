N=len(b:=[int(i.translate({84:48,72:49}),2)for i in[*open(0)][1:]])
print(min(sum(min(c:=(i^j).bit_count(),N-c)for j in b)for i in range(2**N)))