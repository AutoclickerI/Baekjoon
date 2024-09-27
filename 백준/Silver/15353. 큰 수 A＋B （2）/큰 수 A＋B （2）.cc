#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string A, B;
	cin >> A >> B;
	int Ai = A.length() - 1, Bi = B.length() - 1, c = 0, tmp;
	vector<int> arr;
	while (0 <= Ai || 0 <= Bi) {
		tmp = c;
		if (0 <= Ai)
			tmp += A[Ai--] - 48;
		if (0 <= Bi)
			tmp += B[Bi--] - 48;
		c = tmp > 9;
		tmp -= 10 * c;
		arr.push_back(tmp);
	}
	if (c)
		arr.push_back(c);
	for (int i = arr.size() - 1; 0 <= i; i--)
		cout << arr[i];
}