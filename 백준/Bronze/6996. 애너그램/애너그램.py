S=sorted
for s in[*open(0)][1:]:a,b=s.split();print(a,'&',b,'are'+' NOT'*(S(a)!=S(b)),'anagrams.')