package main

import (
	"fmt"
	"reflect"
)

func get_ptr() *int {
	var ptr *int
	fmt.Println("ptr 的值为: %x", ptr)
	// panic: runtime error: invalid memory address or nil pointer dereference
	// fmt.Println("ptr 的*值为: %d", *ptr)
	return ptr
}

func get_ptr_list() *int {
	const MAX int = 3
	var a = [3]int{10, 100, 200}
	var i int
	var ptr [MAX]*int
	var ptr_list *int

	for i = 0; i < MAX; i++ {
		ptr[i] = &a[i]
	}
	for i = 0; i < MAX; i++ {
		fmt.Println("a[%d] = %d: ", i, *ptr[i])
	}
	fmt.Println("type: ", reflect.TypeOf(ptr))
	fmt.Println("i: ", i)
	ptr_list = &i
	pptr_list := &ptr[1]
	fmt.Println("pptr_list: ", pptr_list, ptr_list, *pptr_list, **pptr_list)
	return ptr_list
}

func main() {
	var a int = 10
	var ip *int

	fmt.Println("变量的地址: %x:", &a)
	ip = &a /* 指针变量的存储地址 */
	fmt.Println("ip 变量存储的指针地址: %x:", ip)
	fmt.Println("*ip 变量的值 %d:", *ip)
	ptr := get_ptr()
	if ptr == nil {
		ptr = &a
	}
	fmt.Println("get_ptr返回值: ", ptr, "->", *ptr)
	ptr_list := get_ptr_list()
	fmt.Println("get_ptr_list返回值: ", ptr_list, "->", *ptr_list)
}
