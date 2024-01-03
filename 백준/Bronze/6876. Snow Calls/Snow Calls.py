for _ in[0]*int(input()):
    s=[*input().replace('-','')]
    for i in range(10):
        if 64<ord(s[i])<68:
            s[i]='2'
        if 67<ord(s[i])<71:
            s[i]='3'
        if 70<ord(s[i])<74:
            s[i]='4'
        if 73<ord(s[i])<77:
            s[i]='5'
        if 76<ord(s[i])<80:
            s[i]='6'
        if 79<ord(s[i])<84:
            s[i]='7'
        if 83<ord(s[i])<87:
            s[i]='8'
        if 86<ord(s[i])<91:
            s[i]='9'
    print(*s[:3],'-',*s[3:6],'-',*s[6:10],sep='')