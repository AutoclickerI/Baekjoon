s=input().upper()
if all(i in '\'-!#$%&()@^_{}.~QAZWSXEDCRFVTGBYHNUJMIKOLP1234567890' for i in s) and s.count('.')<2 and len(s.split('.')[0])<9 and ('.'not in s or len(s.split('.')[1])<4):
    print(s)
else:
    s=s.replace(' ','')
    for i in'"/\[]:;=,':s=s.replace(i,'_')
    s=s.rstrip('.')
    idx=s.rfind('.')
    if idx<0:
        print(s[:6]+'~1')
    else:
        a=''
        for i,c in enumerate(s):
            if c!='.' or i==idx:a+=c
        print(a.split('.')[0][:6]+'~1.'+a.split('.')[1][:3])