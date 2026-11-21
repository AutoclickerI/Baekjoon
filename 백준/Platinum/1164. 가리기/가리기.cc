#include <iostream>
#include <vector>
using namespace std;

int p, q, r = 0;
string st;
vector<string> l;
void action(int y, int x, char s, bool a) {
	if (a)l[y][x] = l[y][x + 1] = s;
	else l[y][x] = l[y + 1][x] = l[y + 1][x + 1] = l[y + 1][x + 2] = l[y + 1][x + 3] = l[y][x + 3] = s;
}
bool checkaction(int y, int x, bool a) {
	return a ? (x < q - 1) && (y < p) && (l[y][x] == 'X') && (l[y][x + 1] == 'X') : (x < q - 3) && (y < p - 1) && (l[y][x] == 'X') && (l[y + 1][x] == 'X') && (l[y + 1][x + 1] == 'X') && (l[y + 1][x + 2] == 'X') && (l[y + 1][x + 3] == 'X') && (l[y][x + 3] == 'X');
}
void DFS(int y, int x) {
	if (y > r)r = y;
	if (y > p - 1 || r - y > 1) throw int(1);
	if (x > q - 1) {
		DFS(y + 1, 0);
		return;
	}
	if (l[y][x] != 'X')
		DFS(y, x + 1);
	else {
		if (checkaction(y, x, 0)) {
			action(y, x, 'A', 0);
			DFS(y, x + 1);
			action(y, x, 'X', 0);
		}
		if (checkaction(y, x, 1)) {
			action(y, x, 'B', 1);
			DFS(y, x + 2);
			action(y, x, 'X', 1);
		}
	}
}

int main() {
	cin >> p >> q;
	for (int i = 0; i < p; i++) {
		cin >> st;
		l.push_back(st);
	}
	try {
		DFS(0, 0);
	}
	catch (...) {};
	bool flag = true;
	for (int i = 0; i < p; i++)
		for (int j = 0; j < q; j++)
			if (l[i][j] == 'X')
				flag = false;
	if (flag)
		for (int i = 0; i < p; i++)
			cout << l[i] << endl;
	else cout << -1;
}