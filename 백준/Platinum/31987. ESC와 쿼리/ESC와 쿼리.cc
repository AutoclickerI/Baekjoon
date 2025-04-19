#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 MOD = 1000000007;

struct C {
    int64 p, q;
};

// (a + bi) * (c + di) mod MOD
inline C cmul(const C &a, const C &b) {
    return {
        ( (a.p * b.p % MOD) - (a.q * b.q % MOD) + MOD ) % MOD,
        ( (a.p * b.q % MOD) + (a.q * b.p % MOD) ) % MOD
    };
}

// (a + bi) + (c + di) mod MOD
inline C cadd(const C &a, const C &b) {
    return { (a.p + b.p) % MOD, (a.q + b.q) % MOD };
}

// (a + bi) - (c + di) mod MOD
inline C csub(const C &a, const C &b) {
    return { (a.p - b.p + MOD) % MOD, (a.q - b.q + MOD) % MOD };
}

// fast exponentiation for a scalar mod
int64 modpow(int64 x, int64 e) {
    int64 r = 1;
    x %= MOD;
    while (e) {
        if (e & 1) r = r * x % MOD;
        x = x * x % MOD;
        e >>= 1;
    }
    return r;
}

// modular inverse of (a+bi) via conj/(a^2 + b^2)
C cinv(const C &a) {
    int64 x = a.p, y = a.q;
    int64 denom = (x*x + y*y) % MOD;
    int64 invd = modpow(denom, MOD-2);
    return { x * invd % MOD, (MOD - y) * invd % MOD };
}

// fast exponentiation for complex mod
C cpow(C base, int64 exp) {
    C res{1, 0};
    while (exp) {
        if (exp & 1) res = cmul(res, base);
        base = cmul(base, base);
        exp >>= 1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    // base = (1, -2)  ==  1 - 2i  mod MOD
    C base{ 1, MOD - 2 };
    C one{ 1, 0 };

    while (Q--) {
        int64 i, j, k;
        cin >> i >> j >> k;

        // t = (1 - 2i)^k
        C t = cpow(base, k);

        // numerator = t^(j+1) - t^i
        C num = csub(cpow(t, j + 1), cpow(t, i));

        // denominator inverse = 1 / (t - 1)
        C den_inv = cinv(csub(t, one));

        // answer = Re( num * den_inv )
        C ansC = cmul(num, den_inv);

        cout << ansC.p << "\n";
    }

    return 0;
}