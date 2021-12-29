package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	for {
		fmt.Print("working...")
		time.Sleep(time.Second)
		fmt.Println("done")
		<-done
	}
}

func producter(done chan bool) {
	t := time.NewTimer(time.Microsecond * 100)
	for {
		fmt.Print("product...")
		<-t.C
		if len(done) > 5 {
			continue
		}
		fmt.Println("done")
		done <- true
	}
}
func main() {
	done := make(chan bool, 10)
	go producter(done)
	go worker(done)
	done <- true
	time.Sleep(10 * time.Second)
	fmt.Println("hhsahdad")
}
