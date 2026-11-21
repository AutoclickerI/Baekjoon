from itertools import*
print(sum(all(map(str.__ne__,i,i[1:]))for i in{*map(''.join,permutations(input()))}))