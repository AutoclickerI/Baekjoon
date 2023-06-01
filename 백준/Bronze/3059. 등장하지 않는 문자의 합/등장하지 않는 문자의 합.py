for i in[*open(0)][1:]:
    t='QWERTYUIOPASDFGHJKLZXCVBNM'
    for j in i:t=t.replace(j,'')
    print(sum(ord(k)for k in t))