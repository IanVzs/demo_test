package main

import (
	"fmt"
)

func main() {
	// var x, y int = 3, 4
	// var f float64 = math.Sqrt(float64(x*x + y*y))
	// var z uint = uint(f)
	// fmt.Println(x, y, z)
	var f float64

	i := 42
	// f = float64(i)
	// f = i     go_lang\type_tran.go:16:4: cannot use i (type int) as type float64 in assignment
	u := uint(f)
	fmt.Println(i, f, u)
}
