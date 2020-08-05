package main

import (
	"fmt"
	"time"
)

func main() {

	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("Tick at", t)
			}
		}
	}()

	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true
	fmt.Println("Ticker stopped")
}

/****
>>>
Tick at 2020-05-29 09:52:43.2924217 +0800 CST m=+0.500988701
Tick at 2020-05-29 09:52:43.7921224 +0800 CST m=+1.000689501
Tick at 2020-05-29 09:52:44.2934307 +0800 CST m=+1.501998401

相差大概500ms 返回时间...
Ticker stopped
**/
