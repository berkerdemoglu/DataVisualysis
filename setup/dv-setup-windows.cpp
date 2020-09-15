#include <iostream>

using namespace std;

int main() {
	// Upgrade pip.
	system("pip install -U --upgrade pip");

	// Install the required modules.
	system("pip install -U numpy");
	system("pip install -U requests");
	system("pip install -U matplotlib");
	system("pip install -U mplcursors");

	return 0;
}
