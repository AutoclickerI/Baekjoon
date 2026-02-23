#include <bits/stdc++.h>
using namespace std;

static constexpr int64_t BASE = 1000000000LL; // 1e9 (match Python)
static constexpr int CHUNK_LEN = 9;

struct NumRef {
    uint32_t off;   // offset in pool (LS chunk first)
    uint32_t len;   // number of chunks
    int8_t sign;    // +1 or -1
};

struct BigCanon {
    // Canonical: digits in [0, BASE), sign in {+1,-1}, zero => sign=+1, di={0}
    vector<int32_t> di;
    int8_t sign;

    BigCanon() : di(1, 0), sign(1) {}
};

static inline void trim_zeros(vector<int32_t>& v) {
    while (v.size() > 1 && v.back() == 0) v.pop_back();
}

static inline bool is_zero(const vector<int32_t>& v) {
    return v.size() == 1 && v[0] == 0;
}

static int cmp_big(const BigCanon& a, const BigCanon& b) {
    if (a.sign != b.sign) return (a.sign < b.sign) ? -1 : +1;

    if (a.di.size() != b.di.size()) {
        if (a.sign > 0) return (a.di.size() < b.di.size()) ? -1 : +1;
        return (a.di.size() < b.di.size()) ? +1 : -1;
    }

    for (size_t i = a.di.size(); i-- > 0;) {
        if (a.di[i] == b.di[i]) continue;
        if (a.sign > 0) return (a.di[i] < b.di[i]) ? -1 : +1;
        return (a.di[i] < b.di[i]) ? +1 : -1;
    }
    return 0;
}

static void print_big(const BigCanon& x) {
    if (is_zero(x.di)) {
        cout << "0\n";
        return;
    }
    if (x.sign < 0) cout << '-';
    cout << (int64_t)x.di.back();
    for (size_t i = x.di.size() - 1; i-- > 0;) {
        string s = to_string((int64_t)x.di[i]);
        if ((int)s.size() < CHUNK_LEN) cout << string(CHUNK_LEN - s.size(), '0');
        cout << s;
    }
    cout << "\n";
}

// Normalize bounded signed digits (each digit fits in int32, can be negative),
// into canonical (sign + digits in [0,BASE)).
static BigCanon normalize_signed_digits(vector<int32_t> d) {
    // Remove trailing zeros to determine sign
    trim_zeros(d);
    BigCanon out;

    if (is_zero(d)) {
        out.di = {0};
        out.sign = 1;
        return out;
    }

    int8_t sgn = (d.back() < 0) ? -1 : +1;
    if (sgn < 0) {
        for (auto& v : d) v = (int32_t)(-(int64_t)v);
    }

    // Carry/borrow propagation (using >= BASE)
    // Ensure there is room for carry
    d.push_back(0);
    for (size_t i = 0; i + 1 < d.size(); ++i) {
        int64_t x = (int64_t)d[i];

        if (x < 0) {
            // borrow = ceil(-x / BASE)
            int64_t borrow = (-x + BASE - 1) / BASE;
            x += borrow * BASE;
            d[i + 1] = (int32_t)((int64_t)d[i + 1] - borrow);
        } else if (x >= BASE) {
            int64_t carry = x / BASE;
            x -= carry * BASE;
            d[i + 1] = (int32_t)((int64_t)d[i + 1] + carry);
        }

        d[i] = (int32_t)x;
    }

    // The last digit might still be out of range; extend until stable
    while (true) {
        trim_zeros(d);
        if (d.size() == 1 && d[0] == 0) {
            out.di = {0};
            out.sign = 1;
            return out;
        }

        // if ms digit negative, flip sign and retry (matches Python normalize behavior)
        if (d.back() < 0) {
            sgn = (int8_t)(-sgn);
            for (auto& v : d) v = (int32_t)(-(int64_t)v);
            if (d.size() == 0) d.push_back(0);
            if (d.size() == 1 && d[0] == 0) break;
            d.push_back(0);
            for (size_t i = 0; i + 1 < d.size(); ++i) {
                int64_t x = (int64_t)d[i];
                if (x < 0) {
                    int64_t borrow = (-x + BASE - 1) / BASE;
                    x += borrow * BASE;
                    d[i + 1] = (int32_t)((int64_t)d[i + 1] - borrow);
                } else if (x >= BASE) {
                    int64_t carry = x / BASE;
                    x -= carry * BASE;
                    d[i + 1] = (int32_t)((int64_t)d[i + 1] + carry);
                }
                d[i] = (int32_t)x;
            }
            continue;
        }

        // ms digit is non-negative; check if all digits in [0, BASE)
        bool ok = true;
        for (auto v : d) {
            if (v < 0 || (int64_t)v >= BASE) { ok = false; break; }
        }
        if (ok) break;

        // one more propagation pass if needed
        d.push_back(0);
        for (size_t i = 0; i + 1 < d.size(); ++i) {
            int64_t x = (int64_t)d[i];
            if (x < 0) {
                int64_t borrow = (-x + BASE - 1) / BASE;
                x += borrow * BASE;
                d[i + 1] = (int32_t)((int64_t)d[i + 1] - borrow);
            } else if (x >= BASE) {
                int64_t carry = x / BASE;
                x -= carry * BASE;
                d[i + 1] = (int32_t)((int64_t)d[i + 1] + carry);
            }
            d[i] = (int32_t)x;
        }
    }

    trim_zeros(d);
    if (is_zero(d)) {
        out.di = {0};
        out.sign = 1;
        return out;
    }

    out.di = std::move(d);
    out.sign = sgn;
    return out;
}

// Kadane-like accumulator using the same “single-step” adjustment logic as your Python __iadd__
// and using >= BASE for overflow.
struct Acc {
    vector<int32_t> di;
    int8_t sign;

    Acc() : di(1, 0), sign(1) {}

    int getsign() const {
        int extra = (di.back() < 0) ? -1 : +1;
        return (int)sign * extra;
    }

    void trim() {
        while (di.size() > 1 && di.back() == 0) di.pop_back();
        if (di.size() == 1 && di[0] == 0) sign = 1;
    }

    template<class Pool>
    void assign_from(const Pool& pool, const NumRef& a) {
        di.assign(a.len ? a.len : 1u, 0);
        for (uint32_t i = 0; i < a.len; ++i) di[i] = pool[a.off + i];
        if (di.empty()) di.push_back(0);
        sign = a.sign;
        trim();
    }

    template<class Pool>
    void add_inplace(const Pool& pool, const NumRef& b) {
        if (di.size() < b.len) di.resize(b.len, 0);

        for (size_t i = 0; i < di.size(); ++i) {
            bool f = true;

            if (i < b.len) {
                int64_t v = (int64_t)di[i] + (int64_t)pool[b.off + (uint32_t)i] * (int64_t)sign * (int64_t)b.sign;
                di[i] = (int32_t)v;
                f = false;
            }

            if ((int64_t)di[i] <= -BASE) {
                f = false;
                di[i] = (int32_t)((int64_t)di[i] + BASE);
                if (i + 1 == di.size()) di.push_back(-1);
                else di[i + 1] = (int32_t)((int64_t)di[i + 1] - 1);
            }

            if ((int64_t)di[i] >= BASE) { // keep >= BASE
                f = false;
                di[i] = (int32_t)((int64_t)di[i] - BASE);
                if (i + 1 == di.size()) di.push_back(1);
                else di[i + 1] = (int32_t)((int64_t)di[i + 1] + 1);
            }

            if (f) break;
        }

        trim();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    // Use vector pool (lower overhead than deque). To reduce realloc spikes,
    // grow capacity manually in big chunks.
    vector<int32_t> pool;
    pool.reserve(1 << 20);

    auto ensure_capacity = [&](size_t need_more) {
        if (pool.size() + need_more <= pool.capacity()) return;
        size_t cap = pool.capacity();
        size_t want = pool.size() + need_more;
        size_t newcap = max(want, cap + max<size_t>(cap / 2, (1 << 20)));
        pool.reserve(newcap);
    };

    vector<NumRef> nums(n);

    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;

        int start = 0;
        int8_t sgn = 1;
        if (!s.empty() && s[0] == '-') { sgn = -1; start = 1; }

        int digits = (int)s.size() - start;
        uint32_t need_chunks = (digits <= 0) ? 1u : (uint32_t)((digits + CHUNK_LEN - 1) / CHUNK_LEN);

        ensure_capacity(need_chunks);

        uint32_t off = (uint32_t)pool.size();

        for (int p = (int)s.size(); p > start; p -= CHUNK_LEN) {
            int q = max(start, p - CHUNK_LEN);
            int64_t chunk = 0;
            for (int k = q; k < p; ++k) chunk = chunk * 10 + (s[k] - '0');
            pool.push_back((int32_t)chunk);
        }

        uint32_t len = (uint32_t)pool.size() - off;
        if (len == 0) { pool.push_back(0); len = 1; }

        nums[i] = NumRef{off, len, sgn};
    }

    // Forward boundaries
    vector<uint32_t> fbd;
    fbd.reserve(1024);
    fbd.push_back(0);

    Acc cur;
    for (int i = 0; i < n; ++i) {
        if (cur.getsign() > 0) cur.add_inplace(pool, nums[i]);
        else {
            cur.assign_from(pool, nums[i]);
            fbd.push_back((uint32_t)i);
        }
    }
    fbd.push_back((uint32_t)n);

    // Backward boundaries
    vector<uint32_t> bskip;
    bskip.reserve(1024);
    bskip.push_back(0);

    cur = Acc();
    for (int ri = 0; ri < n; ++ri) {
        const NumRef& v = nums[n - 1 - ri];
        if (cur.getsign() > 0) cur.add_inplace(pool, v);
        else {
            cur.assign_from(pool, v);
            bskip.push_back((uint32_t)ri);
        }
    }

    vector<uint32_t> bbd;
    bbd.reserve(bskip.size() + 2);
    for (uint32_t x : bskip) bbd.push_back((uint32_t)(n - x));
    bbd.push_back(0);
    reverse(bbd.begin(), bbd.end());

    BigCanon best;
    bool has_best = false;

    auto eval_segment = [&](uint32_t S, uint32_t E) {
        if (S >= E) return;

        vector<uint32_t> idx;
        idx.reserve(E - S);
        for (uint32_t k = S; k < E; ++k) idx.push_back(k);

        sort(idx.begin(), idx.end(), [&](uint32_t a, uint32_t b) {
            return nums[a].len > nums[b].len;
        });

        uint32_t maxLen = nums[idx[0]].len;

        // Build bounded signed digits per position using trunc division,
        // then normalize to canonical (sign + [0,BASE) digits).
        vector<int32_t> d;
        d.reserve((size_t)maxLen + 4);

        size_t active = idx.size();
        __int128 carry = 0;

        for (uint32_t pos = 0; pos < maxLen; ++pos) {
            while (active > 0 && nums[idx[active - 1]].len == pos) --active;

            __int128 s = carry;
            for (size_t t = 0; t < active; ++t) {
                const NumRef& a = nums[idx[t]];
                s += (__int128)(int64_t)pool[a.off + pos] * (__int128)a.sign;
            }

            // trunc division to keep remainder in (-BASE, BASE)
            __int128 q = s / (__int128)BASE;
            __int128 r = s - q * (__int128)BASE;
            d.push_back((int32_t)(int64_t)r);
            carry = q;
        }

        while (carry != 0) {
            __int128 q = carry / (__int128)BASE;
            __int128 r = carry - q * (__int128)BASE;
            d.push_back((int32_t)(int64_t)r);
            carry = q;
        }

        BigCanon sum = normalize_signed_digits(std::move(d));

        if (!has_best) {
            best = std::move(sum);
            has_best = true;
        } else if (cmp_big(sum, best) > 0) {
            best = std::move(sum);
        }
    };

    // Two-pointer intersection; evaluate overlaps on the fly
    size_t i = 0, j = 0;
    while (i + 1 < fbd.size() && j + 1 < bbd.size()) {
        uint32_t fS = fbd[i], fE = fbd[i + 1];
        uint32_t bS = bbd[j], bE = bbd[j + 1];

        uint32_t S = max(fS, bS);
        uint32_t E = min(fE, bE);
        if (S < E) eval_segment(S, E);

        if (fE < bE) ++i;
        else ++j;
    }

    // Fallback: max single element
    if (!has_best) {
        for (int k = 0; k < n; ++k) {
            vector<int32_t> d;
            d.reserve(nums[k].len);
            for (uint32_t t = 0; t < nums[k].len; ++t) {
                int32_t v = pool[nums[k].off + t];
                d.push_back(nums[k].sign > 0 ? v : (int32_t)(-(int64_t)v));
            }
            BigCanon x = normalize_signed_digits(std::move(d));
            if (!has_best || cmp_big(x, best) > 0) {
                best = std::move(x);
                has_best = true;
            }
        }
    }

    print_big(best);
    return 0;
}