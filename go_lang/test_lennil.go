package main

import (
	"fmt"
)

func getList() []string {
	return nil
}
func main() {
	a := []string{}
	a = getList()

	fmt.Printf("Len Nil is %d, List is %+v\n", len(a), a)
}
