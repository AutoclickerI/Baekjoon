import sys
input=lambda:sys.stdin.readline()[:-1]

table=[101,127,1009,1013]

l=[i*[0]for i in table]
cnt=[0]*len(table)

def extended_gcd(a, b):
    """
    확장된 유클리드 알고리즘을 사용하여 a * x + b * y = gcd(a, b)를 만족하는 (gcd, x, y)를 반환합니다.
    """
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = extended_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y

def crt_pair(a1, m1, a2, m2):
    """
    두 합동 방정식 x ≡ a1 (mod m1) 및 x ≡ a2 (mod m2)를 풀고,
    x ≡ a (mod lcm(m1, m2)) 형태의 해를 반환합니다.
    """
    g, p, q = extended_gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None, None  # 해가 존재하지 않습니다.
    lcm = m1 * m2 // g
    # k를 구합니다.
    k = ((a2 - a1) // g * p) % (m2 // g)
    x = (a1 + m1 * k) % lcm
    return x, lcm

def find_min_n():
    """
    주어진 table과 remainder 리스트를 사용하여 가장 작은 양수 n을 찾습니다.
    """
    remainder=[i.index(1)for i in l]
    x, m = remainder[0], table[0]
    for i in range(1, len(table)):
        x, m = crt_pair(x, m, remainder[i], table[i])
        if x is None:
            return "해가 존재하지 않습니다."
    return x if x > 0 else x + m
    
s=input()
if s=='resume':
    data=input()[:-1]
    ans=0
    for i in data[::-1]:
        ans*=95
        ans+=ord(i)-32
    db=f'{ans:b}'.zfill(sum(table))
    for i in range(len(table)):
        l[i]=[*map(int,db[:table[i]])]
        db=db[table[i]:]
        cnt[i]=sum(l[i])

for _ in[0]*int(input()):
    n=int(input())
    for i in range(len(table)):
        cnt[i]+=1-l[i][n%table[i]]*2
        l[i][n%table[i]]^=1
    if sum(cnt)==0:
        print(0)
    elif all(i==1 for i in cnt):
        print(find_min_n())
    else:
        print(-1)

if s=='start':
    v=int(''.join(map(str,sum(l,[]))),2)
    s=''
    while v:
        s+=chr(v%95+32)
        v//=95
    print(s+'0')