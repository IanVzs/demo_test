package main

import "fmt"

type A struct {
	A string
	B int
}

func (a A) change(_a string, _b int) {
	a.A = _a
	a.B = _b
	fmt.Println("in: ", a)
}

func (a *A) change2(_a string, _b int) {
	a.A = _a
	a.B = _b
	fmt.Println("in: ", a)
}

func main() {
	a := A{}
	fmt.Println(a)

	a.change("1", 2)
	fmt.Println(a)

	a.change2("1", 2)
	fmt.Println(a)
}
