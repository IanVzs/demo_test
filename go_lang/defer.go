package main

import "fmt"

// defer的堆栈调用和立即求值
func main() {
	a := "init"
	defer fmt.Println("world")
	defer fmt.Println("立即求值, 但函数返回后才会调用: ", a)
	defer fmt.Println("")

	a = "changed"
	fmt.Println("hello")
	fmt.Println("hello ", a)
}

/**
> hello
> hello  changed
> 立即求值, 但函数返回后才会调用:  init
> world
**/
