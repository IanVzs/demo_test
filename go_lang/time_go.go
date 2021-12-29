package main

import (
	"fmt"
	"time"
)

func main() {
	timeUnix := time.Now().Unix()         //单位秒
	timeUnixNano := time.Now().UnixNano() //单位纳秒

	fmt.Println(timeUnix)
	fmt.Println(timeUnixNano)
}
