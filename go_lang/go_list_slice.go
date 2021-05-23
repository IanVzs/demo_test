package main

import (
	"fmt"
	"strings"
)

func sliceShareBaseData() {
	// 切片描述数组, 底层共享, 所以修改同步
	defer fmt.Println("------shareData------")
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println("names befer: ", names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println("a befer: ", a, "b befer: ", b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}

func xo() {
	// 创建一个井字板（经典游戏）
	defer fmt.Println("-----------xoGame---------------")
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// 两个玩家轮流打上 X 和 O
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}
func add2slice(slice []int) []int {
	fmt.Println("befer append: ", slice)
	slice = append(slice, 1)
	fmt.Println("after append: ", slice)
	return slice
}

func claimSlice() {
	defer fmt.Println("-----cliaimSlice------")
	var a_list = [5]int{1, 2, 3, 4}
	fmt.Println("a_list:", a_list, len(a_list), cap(a_list))
	var a_slice = []int{1, 2, 3, 4} //未指定长度就是切片哒
	fmt.Println("a_slice:", a_slice, len(a_slice), cap(a_slice))

	var a_slice2 []int = make([]int, 5) //指定长度就是切片哒
	fmt.Println("a_slice2:", a_slice2, len(a_slice2), cap(a_slice2))

	a_slice3 := make([]int, 5, 7) //切片可以指定长度和最大长度哒
	fmt.Println("a_slice3:", a_slice3, len(a_slice3), cap(a_slice3))
	var a_slice4 = []int{}
	if a_slice4 == nil {
		fmt.Println("hello?!!!")
	} else if a_slice4 != nil {
		fmt.Printf("a_slice4 type:%T\n", a_slice4)
		fmt.Println("a_slice4:", a_slice4, len(a_slice4), cap(a_slice4))
	}
	var numbers []int
	if numbers == nil {
		fmt.Printf("切片是空的::", numbers, "\n")
	}

	fmt.Println("a_slice3:", a_slice3, len(a_slice3), cap(a_slice3))
	a_slice3 = add2slice(a_slice3)
	a_slice3 = add2slice(a_slice3)
	fmt.Println("a_slice3:", a_slice3, len(a_slice3), cap(a_slice3))
	a_slice3 = add2slice(a_slice3)
	a_slice3 = add2slice(a_slice3)
	a_slice3 = add2slice(a_slice3)
	a_slice3 = add2slice(a_slice3)
	fmt.Println("a_slice3:", a_slice3, len(a_slice3), cap(a_slice3))
	add2slice(a_slice4)
	add2slice(a_slice2)
}
func main() {
	claimSlice()
	sliceShareBaseData()
	xo()
}
