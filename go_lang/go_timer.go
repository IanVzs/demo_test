package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Let's Go!\n")
	go func() {
		for i := 0; i < 10; i++ {
			timer1s := time.NewTimer(time.Second)
			<-timer1s.C
			fmt.Println("Timer 1s fired %d loop", i+1)
		}
	}()
	timer2s := time.NewTimer(2 * time.Second)
	<-timer2s.C
	fmt.Println("Timer 2s fired")
	//stop2 := timer2.Stop()
	//if stop2 {
	//	fmt.Println("Timer 2 stopped")
	//}

	time.Sleep(7 * time.Second)
}
