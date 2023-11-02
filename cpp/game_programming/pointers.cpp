#include <iostream>

int main() {
	int i = 6;
	int * p;

	std::cout << i << *p << "\n"; // Segfault;
}
