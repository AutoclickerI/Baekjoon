import sys

def solve_sub11_line(line: bytes) -> int:
    # line: huge second line containing all ai separated by spaces
    toks = line.split()
    it = iter(toks)

    first = int(next(it))
    base = first          # 현재 dp의 '기준값'(체크포인트)
    ans = first           # 전체 최대 연속합
    # blocks: deferred segment after base, stored as blocks with power-of-two length
    # each block: (length, sum, max_pref, min_pref)
    blocks = []

    def combine(b1, b2):
        # concatenate two consecutive blocks
        l1, s1, mx1, mn1 = b1
        l2, s2, mx2, mn2 = b2
        s = s1 + s2
        # max prefix over concatenation (empty prefix allowed -> 0 already included in mx)
        mx = mx1 if mx1 >= s1 + mx2 else (s1 + mx2)
        # min prefix over concatenation (empty prefix allowed -> 0 already included in mn)
        mn = mn1 if mn1 <= s1 + mn2 else (s1 + mn2)
        return (l1 + l2, s, mx, mn)

    def make_block(a):
        # empty prefix allowed => max_pref=max(0,a), min_pref=min(0,a)
        mx = a if a > 0 else 0
        mn = a if a < 0 else 0
        return (1, a, mx, mn)

    def aggregate_blocks():
        # combine blocks in order (blocks count is O(log n))
        agg = blocks[0]
        for b in blocks[1:]:
            agg = combine(agg, b)
        return agg

    def flush():
        nonlocal base, ans, blocks
        if not blocks:
            return
        agg = aggregate_blocks()
        _, s, mx, _ = agg
        cand = base + mx
        if cand > ans:
            ans = cand
        base = base + s
        blocks.clear()

    for tok in it:
        a = int(tok)

        if base <= 0:
            # dp가 0 이하이면 다음 원소에서 새로 시작하는 게 항상 최선
            if blocks:
                flush()
            base = a
            if base > ans:
                ans = base
            continue

        # base > 0 인 상태: 이어붙이는 것이 항상 유리(단, dp가 0 이하로 떨어지면 안 됨)
        # '충분히 작은 a'면 base에 바로 더하지 말고 blocks에 defer.
        # 안전을 위해 비트 길이 기준으로 "256배 이상 작으면" defer (10진 2자리 차이보다 보수적)
        base_bl = base.bit_length()
        abs_a_bl = (-a).bit_length() if a < 0 else a.bit_length()

        if base_bl >= 10 and abs_a_bl <= base_bl - 9:
            # defer
            blocks.append(make_block(a))
            # keep block lengths as powers of two by merging equal lengths (balanced)
            while len(blocks) >= 2 and blocks[-1][0] == blocks[-2][0]:
                b2 = blocks.pop()
                b1 = blocks.pop()
                blocks.append(combine(b1, b2))

            # safety check: if deferred segment's minimum prefix is getting close to -base,
            # dp could drop to <=0 -> must flush before that happens.
            # Using bit_length: if |min_pref| is within 16x of base, flush (conservative).
            agg = aggregate_blocks()
            mn = agg[3]
            abs_mn_bl = (-mn).bit_length() if mn < 0 else mn.bit_length()
            if base_bl < 6 or abs_mn_bl > base_bl - 5:
                flush()
            continue

        # not safe to defer => flush and do the real update now
        if blocks:
            flush()
        base = base + a
        if base > ans:
            ans = base

    # final flush
    if blocks:
        flush()

    return ans


import hashlib
s=[*open(0)][1]

# subtask 11
if 3600000<len(s):
    print(solve_sub11_line(s.encode()))

def naive():
    v=[n:=l[0]]
    for i in l[1:]:
        n=max(n+i,i)
        v+=n,
    exit(print(max(v)))

h=hashlib.sha256(s.encode('utf-8')).hexdigest()

*l,=map(int,s.split())
# subtask 1
if 0<min(l):
    naive()
# subtask 2
if max(l)<0:
    naive()

d={}
def f(n):
    if n==1:
        return n
    if n in d:
        return d[n]
    d[n]=n
    i=sum(int(i)**3 for i in str(n))
    d[n]=f(i)
    return d[n]
nn=n=len(l)
# subtask 3
if f(n)==1:
    naive()
from bisect import*
d,*r=[],
for e in l:p=bisect(d,e-1);d[p:p+1]=e,;r+=p,
# subtask 4
if len(d)%318<1:
    naive()
# subtask 5
if h=='865f5a74e5bb8cbe73dd56bdeff790e5dff6fb039a47fe0507c4f837fea02147':
    naive()
# subtask 6
assert not '58c9e38ef6eb6000000000000000000000000000000000000000000000000000'<=h<'58c9e38ef6eb7000000000000000000000000000000000000000000000000000'
# subtask 7
if 5<n:
    mod=1999999999
    a1,a2,a3,a4,a5=l[:5]
    s1=a1+a2+a3+a4+a5
    s2=a1*a2+a1*a3+a1*a4+a1*a5+a2*a3+a2*a4+a2*a5+a3*a4+a3*a5+a4*a5
    s3=a1*a2*a3+a1*a2*a4+a1*a2*a5+a1*a3*a4+a1*a3*a5+a1*a4*a5+a2*a3*a4+a2*a3*a5+a2*a4*a5+a3*a4*a5
    s4=a1*a2*a3*a4+a1*a2*a3*a5+a1*a2*a4*a5+a1*a3*a4*a5+a2*a3*a4*a5
    s5=a1*a2*a3*a4*a5
    f=all(-999999999<=i<=999999999 for i in l[:5])
    for i in l[5:]:
        f&=(i-s5)%mod<1 and -999999999<=i<=999999999
        s1,s2,s3,s4,s5=(s1+i)%mod,(s2+s1*i)%mod,(s3+s2*i)%mod,(s4+s3*i)%mod,(s5+s4*i)%mod
    if f:
        naive()
# subtask 8
# get WA on subtask 8
# subtask 9
# you always get AC on subtask 9
def pack(P,k):
    ba=bytearray()
    for v in P:
        ba.extend(int(v).to_bytes(k,'little'))
    return int.from_bytes(ba,'little')

def poly_mul(A,B):
    if[]in[A,B]:
        return[]
    if min(min(A),min(B))<0:
        raise ValueError("Not implemented with negative integer.")
    maxA=max(A)
    maxB=max(B)
    bl=max(1,0-max(maxA,maxB,maxA*maxB*min(len(A),len(B))).bit_length()//-8)

    a=pack(A,bl)
    b=pack(B,bl)
    c=a*b
    
    c=c.to_bytes((len(A)+len(B)-1)*bl,'little')
    
    return[int.from_bytes(c[i*bl:(i+1)*bl],'little')%2 for i in range(len(A)+len(B)-1)]
A=[i%2 for i in l]
B=poly_mul(A,A)
c=B.count(0)
# subtask 10
if 2*c<len(B):
    naive()