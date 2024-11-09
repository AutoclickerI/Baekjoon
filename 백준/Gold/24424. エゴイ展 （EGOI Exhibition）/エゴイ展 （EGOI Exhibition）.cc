#include <iostream>

using namespace std;

int N, M, a, v, dp_a;
int tree[600000] = {};


void update(int start, int end, int target, int val, int idx = 1) {
	if (end - start == 1) {
		tree[idx] = val;
		return;
	}
	int mid = (start + end) / 2;
	if (target < mid)
		update(start, mid, target, val, idx * 2);
	else
		update(mid, end, target, val, idx * 2 + 1);
	tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1]);
}

int get_val(int start, int end, int left, int right, int idx = 1) {
	if (end <= left || right <= start || start == end)
		return 0;
	if (left <= start && end <= right)
		return tree[idx];
	int mid = (start + end) / 2;
	return max(get_val(start, mid, left, right, idx * 2), get_val(mid, end, left, right, idx * 2 + 1));
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> a >> v;
		dp_a = get_val(0, M, a - 1, a);
		update(0, M, a - 1, max(v + max(get_val(0, M, 0, a - 1), get_val(0, M, a, M)), dp_a));
	}
	cout << get_val(0, M, 0, M);
}