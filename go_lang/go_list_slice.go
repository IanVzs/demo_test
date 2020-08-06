package main

import "fmt"

func add2slice(slice []int) []int {
	fmt.Println("befer append: ", slice)
	slice = append(slice, 1)
	fmt.Println("after append: ", slice)
	return slice
}
func main() {
	var a_list = [5]int{1, 2, 3, 4}
	fmt.Println("a_list:", a_list, len(a_list), cap(a_list))
	var a_slice = []int{1, 2, 3, 4} //未指定长度就是切片哒
	fmt.Println("a_slice:", a_slice, len(a_slice), cap(a_slice))
	var a_slice2 []int = make([]int, 5) //未指定长度就是切片哒
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
