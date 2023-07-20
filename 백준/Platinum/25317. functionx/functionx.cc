#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

class Fraction {
public:
	Fraction(ll num, ll deno) {
		if (num == 0) {
			numerator = num; denominator = 1;
		}
		else {
			if (deno < 0) {
				num *= -1; deno *= -1;
			}
			numerator = num; denominator = deno;
		}
	}
	bool operator<(const Fraction& comp) {
        __int128 n1=numerator, n2=comp.numerator, d1=comp.denominator, d2=denominator;
		return n1 * d1 < n2 * d2;
	}
	bool operator>(const Fraction& comp) {
		__int128 n1=numerator, n2=comp.numerator, d1=comp.denominator, d2=denominator;
		return n1 * d1 > n2 * d2;
	}
	bool operator==(const Fraction& comp) {
		__int128 n1=numerator, n2=comp.numerator, d1=comp.denominator, d2=denominator;
		return n1 * d1 == n2 * d2;
	}
	bool operator<=(const Fraction& comp) {
		__int128 n1=numerator, n2=comp.numerator, d1=comp.denominator, d2=denominator;
		return n1 * d1 <= n2 * d2;
	}
	bool operator>=(const Fraction& comp) {
		__int128 n1=numerator, n2=comp.numerator, d1=comp.denominator, d2=denominator;
		return n1 * d1 >= n2 * d2;
	}
	ll numerator;
	ll denominator;
};

vector<vector<ll>> query;
vector<Fraction> cord = { Fraction(-1000000000000000001,1LL) };
ll n, tmp, de, nu;
int idx;

bool zero_flag = 0;
vector<bool> tree;
vector<bool> visited;

bool get_sum(int s, int e, int i, int f, int t) {
	if ((e < f) or (t < s))
		return 0;
	if ((f <= s) and (e <= t))
		return tree[i];
	int m = (s + e) / 2;
	return get_sum(s, m, 2 * i, f, t) ^ get_sum(m + 1, e, 2 * i + 1, f, t);
}

void update(int s, int e, int i, int w) {
	if ((w < s) or (w > e))
		return;
	tree[i] = !tree[i];
	if (s - e) {
		int m = (s + e) / 2;
		update(s, m, 2 * i, w);
		update(m + 1, e, 2 * i + 1, w);
	}
	return;
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);
	cin >> n;
	while (n--) {
		cin >> tmp;
		if (tmp == 1) {
			cin >> de >> nu;
			if (de)
				cord.push_back(Fraction(-nu, de));
			query.push_back(vector<ll>{tmp, de, nu});
		}
		else {
			cin >> de;
			query.push_back(vector<ll>{tmp, de});
		}
	}
	tree.resize(4 * cord.size(), 0);
	visited.resize(cord.size(), 0);

	sort(cord.begin(), cord.end());
	for (auto Q : query) {
		if (Q.size() > 2) {
			de = Q[1]; nu = Q[2];
			if (de == 0) {
				if (nu > 0)
					continue;
				else if (nu == 0)
					zero_flag = 1;
				else
					update(0, cord.size() - 1, 1, 0);
			}
			else {
				idx = lower_bound(cord.begin(), cord.end(), Fraction(-nu, de)) - cord.begin();
				visited[idx] = 1;
				update(0, cord.size() - 1, 1, idx);
				if (de > 0)
					update(0, cord.size() - 1, 1, 0);
			}
		}
		else {
			if (zero_flag)
				cout << "0\n";
			else {
				nu = Q[1];
				idx = lower_bound(cord.begin(), cord.end(), Fraction(nu, 1)) - cord.begin();
				if (idx != cord.size() and visited[idx] and Fraction(nu, 1) == cord[idx])
					cout << "0\n";
				else {
					if (get_sum(0, cord.size() - 1, 1, 0, idx - 1))
						cout << "-\n";
					else
						cout << "+\n";
				}
			}
		}
	}
}