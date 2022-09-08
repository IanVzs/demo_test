#include <iostream>

template <class T>
bool compare(T t1, T t2) {
		return (t1 > t2);
}

int main() {
		std::cout << "Hello" << std::endl;
		std::cout << "int False: " << compare<int>(1, 2) << std::endl;
		std::cout << "float True: " << compare<float>(1.2, 1.1) << std::endl;
		return 0;
}
