#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;
int x, y;
set<pair<int, int> > s;
int get_num(int i, int j) {
	if (i == j)
		return i > 0 ? (i + j + 1) * (i + j + 1) : (i + j) * (i + j) + 1;
	if (i == -j)
		return i > 0 ? (i - j) * (i - j) - i + j + 1 : (i - j) * (i - j) - i + j + 1;
	if (abs(i) > abs(j))
		return i > 0 ? (2 * i) * (2 * i) - 2 * i + 1 - i - j : (2 * i) * (2 * i) + 1 - i + j;
	return j > 0 ? (2 * j) * (2 * j) + 2 * j + 1 + i + j : (2 * j) * (2 * j) + 1 - i + j;
}
int mi(int a, int b) {
	return get_num(x + a, y + b) + 5000000 * (s.find(make_pair(x + a, y + b)) != s.end());
}
int main() {
	int n, p, q,m,dx,dy;
	char c;
	cin >> n;
	vector<vector<int>> l;
	vector<string> d(n, "");
	for (int i = 0; i < n; i++) {
		cin >> p >> q;
		l.push_back({ i, p, q });
	}
	while (!l.empty()) {
		sort(l.begin(), l.end(), [](vector<int> a, vector<int> b) {return get_num(a[1], a[2]) < get_num(b[1], b[2]); });
		p = 0;
		s.clear();
		while (p < l.size()) {
			x = l[p][1]; y = l[p][2];
			if (x == 0 && y == 0) {
				l.erase(l.begin() + p);
				continue;
			}
			m = mi(-1, -1);
			c = 'Z';
			dx = dy = -1;
			if (mi(-1, 0) < m) {
				m = mi(-1, 0);
				c = 'A';
				dy = 0;
			}
			if (mi(-1, 1) < m) {
				m = mi(-1, 1);
				c = 'Q';
				dy = 1;
			}
			if (mi(0, -1) < m) {
				m = mi(0, -1);
				c = 'X';
				dx = 0;
				dy = -1;
			}
			if (mi(0, 1) < m) {
				m = mi(0, 1);
				c = 'W';
				dx = 0;
				dy = 1;
			}
			if (mi(1, -1) < m) {
				m = mi(1, -1);
				c = 'C';
				dx = 1;
				dy = -1;
			}
			if (mi(1, 0) < m) {
				m = mi(1, 0);
				c = 'D';
				dx = 1;
				dy = 0;
			}
			if (mi(1, 1) < m) {
				m = mi(1, 1);
				c = 'E';
				dx = 1;
				dy = 1;
			}
			d[l[p][0]] += c;
			s.insert(make_pair(x + dx, y + dy));
			l[p][1] += dx;
			l[p][2] += dy;
			p += 1;
		}
	}
	for (auto s : d)
		cout << s << endl;
}