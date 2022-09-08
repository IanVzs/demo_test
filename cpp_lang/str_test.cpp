/**
 *目标数组 dest 不够大，而源字符串的长度又太长，可能会造成缓冲溢出的情况
 * **/

#include <iostream>
#include <string.h>
#include <string>
int strcpy_test() {
		char str1[] = "niubile666";
		char str2[] = "lihaile";
		char str3[] = "niubile666";
		char str4[] = "lihaile";

		strcpy(str3, str4);
		std::cout << "str3: " << str3 << "\t strlen: " << strlen(str3) << std::endl;
		std::cout << "str4: " << str4 << "\t strlen: " << strlen(str4) << std::endl;

		strcpy(str2, str1);
		std::cout << "str1: " << str1 << std::endl;
		std::cout << "str2: " << str2 << std::endl;

		std::cout << "str3: " << str3 << "\t strlen: " << strlen(str3) << std::endl;
		std::cout << "str4: " << str4 << "\t strlen: " << strlen(str4) << std::endl;

		return 0;
}

// 幸福的大门
void string_test() {
		using namespace std;
		string str1 = "C++ 标准库提供了 string 类类型，支持上述所有的操作，另外还增加了其他更多的功能";
		string str2 = "Niubia bia a";
		string str3;
		int len;
		int index;

		str3 = str1 + str2;
		cout << "str3(+&=): " << str3 << endl;

		str3 = str2;
		cout << "str3(=): " << str3 << endl;

		len = str3.size();
		cout << "str3 size长度: " << len << endl;
		len = str3.length();
		cout << "str3 length长度: " << len << endl;

		str2.append(" /append to str2");
		cout << "str2(append): " << str2 << endl;
		cout << "str3(after str2 append): " << str3 << endl;

		std::cout << "------------------------find----------------------------" << std::endl;
		index = str3.find("bia");
		str3.replace(index, 2, ""); // 从index后2个字符替换成空
		cout << "str3 after replace: " << str3 << endl;

		/**注意 find_first(last)_of不是按完全匹配的，是按单个字母位置最优先匹配的**/
		int first = str2.find_first_of("bbbbb");
		int last = str2.find_last_of("aaaaa");
		cout << "str2(" << str2 << ") 最开始一个(" << first << ")和最后一个(" << last << ")中间值: " << str2.substr(first, last) << endl;

}
int main() {
		strcpy_test();
		std::cout << "-------------------------人生苦短，多用标准库----------------------------" << std::endl;
		string_test();
}
