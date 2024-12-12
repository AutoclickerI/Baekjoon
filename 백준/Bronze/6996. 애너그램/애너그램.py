from collections import*
C=Counter
for i in[*open(0)][1:]:p,q=i.split();print(p,'&',q,'are'+' NOT'*(C(p)!=C(q)),'anagrams.')