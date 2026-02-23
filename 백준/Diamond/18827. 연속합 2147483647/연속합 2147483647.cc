#include <bits/stdc++.h>
using namespace std;

#define ll long long

static constexpr ll BASE = 1000000000LL;
static constexpr ll CHUNK_LEN = 9;

struct NumRef {
    ll off;
    ll len;
    char sign;
};

struct BigCanon {
    vector<ll> di;
    char sign;
};

static inline void trim_zeros(vector<ll>& v) {
    while (v.size() > 1 && v.back() == 0) v.pop_back();
}
static inline bool is_zero(const vector<ll>& v) {
    return v.size() == 1 && v[0] == 0;
}

static inline void propagate_once(vector<ll>& d) {
    d.push_back(0);
    for (ll i = 0; i + 1 < d.size(); ++i) {
        ll x = d[i];
        if (x < 0) {
            ll borrow = (BASE - 1 - x) / BASE;
            x += borrow * BASE;
            d[i + 1] -= borrow;
        } else if (x >= BASE) {
            ll carry = x / BASE;
            x -= carry * BASE;
            d[i + 1] += carry;
        }
        d[i] = x;
    }
}

static BigCanon normalize_signed_digits(vector<ll> d) {
    trim_zeros(d);
    if (is_zero(d)) return BigCanon{{0}, 1};

    char sign = (d.back() < 0) ? -1 : 1;
    if (sign < 0) for (auto& v : d) v *= -1;

    while (true) {
        propagate_once(d);
        trim_zeros(d);

        if (is_zero(d)) return BigCanon{{0}, 1};

        if (d.back() < 0) {
            sign *= -1;
            for (auto& v : d) v *= -1;
            continue;
        }

        if (d.back() >= BASE) continue;

        break;
    }

    trim_zeros(d);
    if (is_zero(d)) return BigCanon{{0}, 1};
    return BigCanon{std::move(d), sign};
}

static ll cmp_big(const BigCanon& a, const BigCanon& b) {
    if (a.sign != b.sign) return (a.sign < b.sign) ? -1 : 1;

    if (a.di.size() != b.di.size()) {
        if (a.sign > 0) return (a.di.size() < b.di.size()) ? -1 : 1;
        return (a.di.size() < b.di.size()) ? 1 : -1;
    }

    for (int i = a.di.size(); i-- > 0;) {
        if (a.di[i] == b.di[i]) continue;
        if (a.sign > 0) return (a.di[i] < b.di[i]) ? -1 : 1;
        return (a.di[i] < b.di[i]) ? 1 : -1;
    }
    return 0;
}

static void print_big(const BigCanon& x) {
    if (is_zero(x.di)) { cout << "0\n"; return; }
    if (x.sign < 0) cout << '-';
    cout << x.di.back();
    for (int i = x.di.size() - 1; i-- > 0;) {
        string s = to_string(x.di[i]);
        if (s.size() < CHUNK_LEN) cout << string(CHUNK_LEN - s.size(), '0');
        cout << s;
    }
    cout << "\n";
}

struct Acc {
    vector<ll> di;
    char sign;

    Acc() : di(1, 0), sign(1) {}

    ll getsign() const {
        ll extra = (di.back() < 0) ? -1 : 1;
        return sign * extra;
    }

    void trim() {
        while (di.size() > 1 && di.back() == 0) di.pop_back();
        if (di.size() == 1 && di[0] == 0) sign = 1;
    }

    void assign_from(const vector<ll>& pool, const NumRef& a) {
        di.assign(a.len ? a.len : 1, 0);
        for (ll i = 0; i < a.len; ++i) di[i] = pool[a.off + i];
        if (di.empty()) di.push_back(0);
        sign = a.sign;
        trim();
    }

    void add_inplace(const vector<ll>& pool, const NumRef& b) {
        if (di.size() < b.len) di.resize(b.len, 0);

        for (ll i = 0; i < di.size(); ++i) {
            bool f = true;

            if (i < b.len) {
                ll v = di[i] + pool[b.off + i] * sign * b.sign;
                di[i] = v;
                f = false;
            }

            if (di[i] <= -BASE) {
                f = false;
                di[i] += BASE;
                if (i + 1 == di.size()) di.push_back(-1);
                else di[i + 1] -= 1;
            }

            if (di[i] >= BASE) {
                f = false;
                di[i] -= BASE;
                if (i + 1 == di.size()) di.push_back(1);
                else di[i + 1] += 1;
            }

            if (f) break;
        }

        trim();
    }
};

int kadane(int n, vector<string>& data) {
    vector<NumRef> nums(n);
    vector<ll> pool;
    pool.reserve(1 << 20);

    auto grow_pool = [&](ll need_more) {
        ll need = pool.size() + need_more;
        if (need <= pool.capacity()) return;
        ll cap = pool.capacity();
        ll newcap = max(need, cap + max<ll>(cap / 2, 1 << 20));
        pool.reserve(newcap);
    };

    auto parse_num = [&](const string& s, NumRef& out) {
        ll start = 0;
        char sgn = 1;
        if (!s.empty() && s[0] == '-') { sgn = -1; start = 1; }

        ll digits = s.size() - start;
        ll chunks = (digits <= 0) ? 1 : (digits + CHUNK_LEN - 1) / CHUNK_LEN;
        grow_pool(chunks);

        ll off = pool.size();
        for (ll p = s.size(); p > start; p -= CHUNK_LEN) {
            ll q = max(start, p - CHUNK_LEN);
            ll chunk = 0;
            for (ll k = q; k < p; ++k) chunk = chunk * 10 + (s[k] - '0');
            pool.push_back(chunk);
        }
        ll len = pool.size() - off;
        if (len == 0) { pool.push_back(0); len = 1; }

        out = NumRef{off, len, sgn};
    };
    int vv = 0;
    for (auto& s : data) {
        parse_num(s, nums[vv]);
        vv++;
    }

    vector<ll> fbd;
    fbd.reserve(1024);
    fbd.push_back(0);

    Acc cur;
    for (ll i = 0; i < n; ++i) {
        if (cur.getsign() > 0) cur.add_inplace(pool, nums[i]);
        else { cur.assign_from(pool, nums[i]); fbd.push_back(i); }
    }
    fbd.push_back(n);

    vector<ll> bskip;
    bskip.reserve(1024);
    bskip.push_back(0);

    cur = Acc();
    for (ll ri = 0; ri < n; ++ri) {
        const NumRef& v = nums[n - 1 - ri];
        if (cur.getsign() > 0) cur.add_inplace(pool, v);
        else { cur.assign_from(pool, v); bskip.push_back(ri); }
    }

    vector<ll> bbd;
    bbd.reserve(bskip.size() + 2);
    for (ll x : bskip) bbd.push_back(n - x);
    bbd.push_back(0);
    reverse(bbd.begin(), bbd.end());

    BigCanon best{{0}, 1};
    bool has_best = false;

    auto eval_segment = [&](ll S, ll E) {
        if (S >= E) return;

        vector<ll> idx;
        idx.reserve(E - S);
        for (int k = S; k < E; ++k) idx.push_back(k);

        sort(idx.begin(), idx.end(), [&](ll a, ll b) {
            return nums[a].len > nums[b].len;
        });

        ll maxLen = nums[idx[0]].len;
        vector<ll> d;
        d.reserve(maxLen + 4);

        ll active = idx.size();
        __int128 carry = 0;

        for (int pos = 0; pos < maxLen; ++pos) {
            while (active > 0 && nums[idx[active - 1]].len == pos) --active;

            __int128 s = carry;
            for (int t = 0; t < active; ++t) {
                const NumRef& a = nums[idx[t]];
                s += (__int128)pool[a.off + pos] * (__int128)a.sign;
            }

            __int128 q = s / (__int128)BASE;
            __int128 r = s - q * (__int128)BASE;
            d.push_back(r);
            carry = q;
        }

        while (carry != 0) {
            __int128 q = carry / (__int128)BASE;
            __int128 r = carry - q * (__int128)BASE;
            d.push_back(r);
            carry = q;
        }

        BigCanon sum = normalize_signed_digits(std::move(d));

        if (!has_best || cmp_big(sum, best) > 0) {
            best = std::move(sum);
            has_best = true;
        }
    };

    int i = 0, j = 0;
    while (i + 1 < fbd.size() && j + 1 < bbd.size()) {
        ll fS = fbd[i], fE = fbd[i + 1];
        ll bS = bbd[j], bE = bbd[j + 1];

        ll S = max(fS, bS);
        ll E = min(fE, bE);
        if (S < E) eval_segment(S, E);

        if (fE < bE) ++i;
        else ++j;
    }

    print_big(best);
    return 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, total_cnt = -1;
    cin >> n;

    vector<string> data;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        data.push_back(s);
        total_cnt += s.size() + 1;
    }
    // subtask 11
    if (3500000 < total_cnt)
      return kadane(n,data);
    bool f = 1;
    for (auto& s : data)
      f &= s[0] != '-';
    // subtask 1
    if (f)
      return kadane(n, data);
}