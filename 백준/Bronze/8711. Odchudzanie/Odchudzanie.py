v=0
print(max(v-int(i)for i in[*open(0)][1].split()if(v:=max(v,int(i)))))