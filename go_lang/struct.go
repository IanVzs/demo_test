package main

import (
	"fmt"
	"reflect"
)

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

	t := reflect.TypeOf(a)
	v := reflect.ValueOf(a)

	fmt.Printf("a Is %+v \n\n", a)
	for i := 0; i < t.NumField(); i++ {
		fmt.Println("t: ", t, "  ---  ", "v: ", v)
		fmt.Println("gogogo\n", t.Field(i), v.Field(i))
		name := t.Field(i).Name
		value := v.Field(i).Interface()
		fmt.Println("show", name, value)
		svalue, ok := value.(int)
		if ok {
			fmt.Println("good vlaue is int: ", svalue)
		}

	}
}
