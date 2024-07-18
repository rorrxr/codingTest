#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	
	int dwarf[9];
	int dwa_sum = 0;

	for (int i = 0; i < 9; i++) {
		cin >> dwarf[i];
		dwa_sum += dwarf[i];
	}

	//cout << "\n결과" << endl;

	sort(dwarf, dwarf + 9);

	for (int i = 0; i < 9; i++) {
		int j = 0;

		for (j = i + j; j < 9; j++) {
			if ((dwa_sum - (dwarf[i] + dwarf[j])) == 100) {
				for (int k = 0; k < 9; k++) {
					if (i == k || j == k) 
						continue;
					cout << dwarf[k] << endl;
				}
				return 0;
			}
		}
	}

}