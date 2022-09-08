/**
 * some about class
**/
#include <iostream>
using namespace std;

class Box
{
		public:
				double length;
				double breadth;
				double height;
				// func claim
				double get();
				int set(double len, double bre, double hei );
				void print();
				// friend void printVolume(Box box);
		private:
				/**
				 * error: ‘double Box::volume’ is private within this context
				 **/
				double volume;
				/**
				 * friend function在哪儿(public/private)声明貌似无所谓
				 * 下面两个方法在调用时使用方法相同:
				 ** 		printVolume(box1);
				 ** 		printVolumePointer(box1);
				 **	但在操作上一个用的是复制来的实例，一个是原实例
				 ** 所以在使用上追求效率的话，还为了保证不被修改，一般搭配const 使用
				 **/
				friend void printVolume(Box box);
				friend void printVolumePointer(const Box& box);

}; // 类定义完需要; namespace不需要

// 获取Box体积
double Box::get() {
		volume = length * breadth * height;
		return volume;
}

// print class item
void Box::print() {
		cout << "Box(height= " << height << ", breadth= " << breadth << ", height= " \
				<< height << ", | volume=" << volume << ")" << endl;
}
void printVolume(Box box) {
		cout << "printVolume box: " << &box << endl;
		printf("volume: %f\n", box.volume);
		box.volume = 999.0;
}
void printVolumePointer(const Box& box) {
		cout << "printVolumePointer box: " << &box << endl;
		printf("volume: %f\n", box.volume);
		// box.volume = 666.0;
}
// 设置长宽高 成功1 失败0
int Box::set(double len, double bre, double hei ) {
		int sign = 0;
		if (len == 0 || bre == 0 || hei == 0) {
				;
		} else {
				length = len;
				breadth = bre;
				height = hei;
				sign = 1;
		}
		return sign;
}


int main() {
		Box box1;
		Box box2;
		int sign;
		double volume1;
		double volume2;
		// 1
		box1.length = 1.0;
		box1.breadth = 1.0;
		box1.height = 1.0;
		printVolume(box1);
		cout << "printVolume box real: " << &box1 << endl;
		// 2
		sign = box2.set(1.0, 2.0, 3.0);
		if (sign == 0) {
				cout << "set error!" << endl;
		} else {
				box2.print();
		}
		volume1 = box1.get();
		volume2 = box2.get();
		printVolume(box1);
		cout << "printVolume box real2222: " << &box1 << endl;
		printVolumePointer(box2);
		// get 中没有endl 这里声明一下结束流;
		cout << endl;
		box1.print();
		box2.print();
		return 0;
}
