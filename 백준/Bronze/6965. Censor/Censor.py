for i in[*open(0)][1:]:print(*[[i,'*'*4][len(i)==4]for i in i.split()],'\n')