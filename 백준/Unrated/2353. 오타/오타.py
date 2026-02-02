cho={*'rsefaqtdwczxvgREQTW'}
jung={*'koiOjpuPhynbml','hk','ho','hl','nj','np','nl','ml'}
jong={*cho}-{*'EQW'}|{'rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt'}

possible={i+j for i in cho for j in jung}|{i+j+k for i in cho for j in jung for k in jong}

prefix={i[:j+1]for i in possible for j in range(len(i))}

possible_pos={0}

s=input()

for i in range(len(s)):
    f=i<1
    for dv in range(1,6):
        if i-dv in possible_pos:
            if s[i-dv:i]in possible:
                possible_pos|={i}
                f=1
            if s[i-dv:i]in prefix:
                f=1
    if not f:
        print(i)
        break
else:
    print(0)