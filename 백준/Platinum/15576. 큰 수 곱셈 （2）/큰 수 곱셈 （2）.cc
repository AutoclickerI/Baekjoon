#include <bits/stdc++.h>

using namespace std;

using ll = long long;

using i128 = __int128_t;

static const ll BASE = 1000000;   // 10^6

static const int BASE_DIG = 6;

// 나눗셈이 없는 leaf가 훨씬 싸므로 CUT을 좀 키워도 됨

static const int CUT = 64;        // 32/64/128 튜닝 가능

// raw naive convolution: res[0..2n-1] += a[0..n-1] * b[0..n-1]

// (carry 정규화 X, 그냥 누적만)

static inline void mul_naive_raw(const ll* a, const ll* b, ll* res, int n) {

    memset(res, 0, sizeof(ll) * (2 * n));

    for (int i = 0; i < n; i++) {

        i128 ai = a[i];

        for (int j = 0; j < n; j++) {

            res[i + j] += (ll)(ai * (i128)b[j]); // n<=CUT이면 overflow 여유 충분

        }

    }

}

// karatsuba for n = power of two

// res size = 2n, work 충분히 크게

// work 요구량 대략 < 8n ll

static void karatsuba_pow2_raw(const ll* a, const ll* b, ll* res, int n, ll* work) {

    if (n <= CUT) {

        mul_naive_raw(a, b, res, n);

        return;

    }

    int m = n >> 1;

    // multiply length m => result length 2m = n

    ll* z0   = work;          // size n

    ll* z1   = work + n;      // size n

    ll* z2   = work + 2 * n;  // size n

    ll* sumA = work + 3 * n;  // size m

    ll* sumB = work + 3 * n + m; // size m

    ll* child = work + 3 * n + 2 * m;

    // z0 = a0*b0

    karatsuba_pow2_raw(a, b, z0, m, child);

    // z2 = a1*b1

    karatsuba_pow2_raw(a + m, b + m, z2, m, child);

    // sumA = a0 + a1, sumB = b0 + b1  (BASE carry는 나중에)

    for (int i = 0; i < m; i++) {

        sumA[i] = a[i] + a[i + m];

        sumB[i] = b[i] + b[i + m];

    }

    // z1 = (a0+a1)(b0+b1)

    karatsuba_pow2_raw(sumA, sumB, z1, m, child);

    // z1 = z1 - z0 - z2  (signed 가능)

    for (int i = 0; i < n; i++) {

        z1[i] -= z0[i];

        z1[i] -= z2[i];

    }

    // res = z0 + (z1 << m) + (z2 << 2m)

    // res length 2n

    memset(res, 0, sizeof(ll) * (2 * n));

    // z0 at offset 0

    for (int i = 0; i < n; i++) res[i] += z0[i];

    // z1 at offset m

    for (int i = 0; i < n; i++) res[i + m] += z1[i];

    // z2 at offset 2m = n

    for (int i = 0; i < n; i++) res[i + n] += z2[i];

}

// floor division for negative numbers: floor(x / BASE)

static inline i128 floordiv(i128 x) {

    if (x >= 0) return x / BASE;

    // floor(-a/BASE) = -ceil(a/BASE)

    i128 a = -x;

    return -((a + BASE - 1) / BASE);

}

// 마지막에 carry를 딱 1번만 수행: v[i]를 [0, BASE)로 정규화

static void normalize_carry(vector<ll>& v) {

    i128 carry = 0;

    for (size_t i = 0; i < v.size(); i++) {

        i128 cur = (i128)v[i] + carry;

        i128 q = floordiv(cur);

        i128 r = cur - q * BASE; // 0 <= r < BASE

        v[i] = (ll)r;

        carry = q;

    }

    while (carry != 0) {

        i128 q = floordiv(carry);

        i128 r = carry - q * BASE;

        v.push_back((ll)r);

        carry = q;

    }

    while (v.size() > 1 && v.back() == 0) v.pop_back();

}

static vector<ll> parse_big(const string& s) {

    vector<ll> a;

    for (int i = (int)s.size(); i > 0; i -= BASE_DIG) {

        int l = max(0, i - BASE_DIG);

        a.push_back(stoll(s.substr(l, i - l)));

    }

    while (a.size() > 1 && a.back() == 0) a.pop_back();

    return a;

}

static int next_pow2(int x) {

    int p = 1;

    while (p < x) p <<= 1;

    return p;

}

int main() {

    ios::sync_with_stdio(false);

    cin.tie(nullptr);

    string A, B;

    cin >> A >> B;

    if (A == "0" || B == "0") {

        cout << 0 << "\n";

        return 0;

    }

    vector<ll> a = parse_big(A);

    vector<ll> b = parse_big(B);

    int n0 = (int)max(a.size(), b.size());

    int n = next_pow2(n0);

    a.resize(n, 0);

    b.resize(n, 0);

    vector<ll> res(2 * n, 0);

    // scratch: 넉넉히 8n

    vector<ll> work(8 * n, 0);

    karatsuba_pow2_raw(a.data(), b.data(), res.data(), n, work.data());

    // carry는 마지막에 1번만

    normalize_carry(res);

    // 출력

    int i = (int)res.size() - 1;

    cout << res[i];

    for (i = i - 1; i >= 0; i--) {

        cout << setw(BASE_DIG) << setfill('0') << res[i];

    }

    cout << "\n";

    return 0;

}