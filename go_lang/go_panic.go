package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("vim-go")
	go_panic()
}

func go_panic() {
	panic("raise a problem....")
	_, err := os.Create("/tmp/file")
	if err != nil {
		panic(err)
	}
}
