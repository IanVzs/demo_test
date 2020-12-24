package main

import (
        "fmt"
        "time"
        )

func test1() {
        fmt.Println("---------------------------------------")
        values := [3][2]int{{1, 1}, {2, 1}, {3, 1}}
        for _, val := range values {
                fmt.Println(val)
        }
}
func test2() {
        // 这种写法里面是有问题的.... 
        fmt.Println("---------------------------------------")
        values := [3][2]int{{1, 3}, {2, 3}, {3, 3}}
        for _n, val := range values {
                fmt.Println(_n)
                fmt.Printf("val Type: %T \n", val)
                go func() {
                        fmt.Println(val)
                }()
        }
}
func test3() {
        // test2 的修补版
        fmt.Println("---------------------------------------")
        values := [3][2]int{{1, 5}, {2, 5}, {3, 5}}
        for _, val := range values {
                go func(val interface{}) {
                        fmt.Println(val)
                }(val)
        }
}
func main() {
        fmt.Println("Hi, 你好.")
        test1()
        test2()
        test3()
        time.Sleep(1 * time.Second)
}
