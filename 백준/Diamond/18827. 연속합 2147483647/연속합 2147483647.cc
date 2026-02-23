#include <bits/stdc++.h>
using namespace std;

struct Big {
    // Base 1e18: limbs are uint64_t, carry uses unsigned __int128
    static constexpr uint64_t BASE = 1000000000000000000ULL; // 1e18
    static constexpr int DIG = 18;

    int sign = 0;              // -1, 0, +1
    vector<uint64_t> a;        // little-endian limbs

    Big() : sign(0), a(1, 0) {}

    inline bool is_pos() const { return sign > 0; }
    inline bool is_zero() const { return sign == 0; }

    void trim() {
        while (a.size() > 1 && a.back() == 0) a.pop_back();
        if (a.size() == 1 && a[0] == 0) sign = 0;
    }

    static Big from_token(const string &s) {
        Big r;
        int n = (int)s.size();
        int i = 0;
        int sg = 1;
        if (n && s[0] == '-') { sg = -1; i = 1; }
        while (i < n && s[i] == '0') i++;
        if (i == n) return Big(); // zero

        r.sign = sg;
        r.a.clear();
        r.a.reserve((n - i + DIG - 1) / DIG);

        for (int end = n; end > i; end -= DIG) {
            int st = max(i, end - DIG);
            uint64_t chunk = 0;
            for (int k = st; k < end; k++) chunk = chunk * 10ULL + (uint64_t)(s[k] - '0');
            r.a.push_back(chunk);
        }
        r.trim();
        return r;
    }

    static int cmp_abs(const Big &x, const Big &y) {
        if (x.a.size() != y.a.size()) return x.a.size() < y.a.size() ? -1 : 1;
        for (int i = (int)x.a.size() - 1; i >= 0; i--) {
            if (x.a[i] != y.a[i]) return x.a[i] < y.a[i] ? -1 : 1;
        }
        return 0;
    }

    static int cmp(const Big &x, const Big &y) {
        if (x.sign != y.sign) return x.sign < y.sign ? -1 : 1;
        if (x.sign == 0) return 0;
        int c = cmp_abs(x, y);
        return x.sign > 0 ? c : -c;
    }

    // a = |a| + |b|
    static void add_abs_inplace(Big &x, const Big &y) {
        size_t n = x.a.size();
        if (x.a.size() < y.a.size()) x.a.resize(y.a.size(), 0);

        unsigned __int128 carry = 0;
        size_t i = 0;
        // Only iterate while there is RHS limb or carry; do not scan full x if y is short.
        for (; i < y.a.size() || carry; i++) {
            if (i == x.a.size()) x.a.push_back(0);
            unsigned __int128 sum = (unsigned __int128)x.a[i] + (i < y.a.size() ? y.a[i] : 0ULL) + carry;
            if (sum >= BASE) { sum -= BASE; carry = 1; }
            else carry = 0;
            x.a[i] = (uint64_t)sum;
        }
        // no need to touch remaining higher limbs
    }

    // assumes |x| >= |y|, x = |x| - |y|
    static void sub_abs_inplace(Big &x, const Big &y) {
        long long borrow = 0;
        size_t i = 0;
        // Only iterate while there is RHS limb or borrow
        for (; i < y.a.size() || borrow; i++) {
            unsigned __int128 xi = x.a[i];
            unsigned __int128 yi = (i < y.a.size() ? y.a[i] : 0ULL);
            // xi - yi - borrow in signed sense
            __int128 cur = (__int128)xi - (__int128)yi - (__int128)borrow;
            if (cur < 0) { cur += (__int128)BASE; borrow = 1; }
            else borrow = 0;
            x.a[i] = (uint64_t)cur;
        }
        x.trim();
    }

    // Add other into *this; other is rvalue so we can move its limbs if needed.
    void iadd(Big &&other) {
        if (other.sign == 0) return;
        if (sign == 0) { sign = other.sign; a = std::move(other.a); return; }

        if (sign == other.sign) {
            add_abs_inplace(*this, other);
            return;
        }

        int c = cmp_abs(*this, other);
        if (c == 0) {
            sign = 0;
            a.assign(1, 0);
        } else if (c > 0) {
            sub_abs_inplace(*this, other);
            // sign stays
        } else {
            // result = |other| - |this|, sign = other.sign; we can move other.a
            Big tmp;
            tmp.sign = other.sign;
            tmp.a = std::move(other.a);
            sub_abs_inplace(tmp, *this);
            *this = std::move(tmp);
        }
    }

    string to_string() const {
        if (sign == 0) return "0";
        ostringstream oss;
        if (sign < 0) oss << '-';
        oss << a.back();
        for (int i = (int)a.size() - 2; i >= 0; i--) {
            oss << setw(DIG) << setfill('0') << a[i];
        }
        return oss.str();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    // Replace this with your fast scanner if you want; WA is independent of I/O speed.
    string tok;

    Big cur;
    Big best_owned;          // stores best when it can't safely alias cur
    bool best_aliases_cur = false;

    for (int i = 0; i < n; i++) {
        cin >> tok;
        Big x = Big::from_token(tok);

        if (i == 0) {
            cur = std::move(x);
            best_aliases_cur = true;  // best == cur
            continue;
        }

        if (!cur.is_pos()) {
            // We will overwrite cur with x. If best aliases cur and x < cur(old), we must snapshot old cur.
            if (best_aliases_cur && Big::cmp(x, cur) < 0) {
                best_owned = cur;          // snapshot old best
                best_aliases_cur = false;  // best is now best_owned
            }
            cur = std::move(x);
        } else {
            // cur > 0, we will do cur += x
            if (best_aliases_cur && x.sign < 0) {
                best_owned = cur;          // snapshot old best (will be decreased)
                best_aliases_cur = false;
            }
            cur.iadd(std::move(x));
        }

        // Update best if cur is larger than current best
        const Big& best_ref = best_aliases_cur ? cur : best_owned;
        if (Big::cmp(cur, best_ref) > 0) {
            best_aliases_cur = true;       // best becomes cur, no copy
        }
    }

    cout << (best_aliases_cur ? cur.to_string() : best_owned.to_string()) << "\n";
    return 0;
}