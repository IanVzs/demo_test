/**
 * use namespace to avoid that
 ** error: redefinition of ‘void print_hello()’
**/
#include <iostream>
using namespace std;

namespace en {
		void print_hello() {
				cout << "Hello" << endl;
		}
}

namespace zh_CN {
		void print_hello() {
				cout << "你好" << endl;
		}
}

void print_hello() {
		cout << "hello world" << endl;
}

int main() {
		print_hello();
		en::print_hello();
		zh_CN::print_hello();
		return 0;
}
