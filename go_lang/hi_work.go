package main

import (
	"fmt"
)

func main() {
	var w = []int{1, 2, 3, 4, 5, 6, 7}
	var a = w[2:]
	fmt.Println(len(a), cap(a), a)
	fmt.Printf("%p, %p\n", &w, &a)
	fmt.Printf("%p, %p\n", &w[6], &a[4])
	var b = w[:2]
	fmt.Println(len(b), cap(b), b)
	fmt.Printf("%p, %p\n", &w, &b)
	var c = w[1:2]
	fmt.Println(len(c), cap(c), c)
	var d = w[:4]
	fmt.Println(len(d), cap(d), d)
	fmt.Printf("d befer: %p\n", &d)
	d = append(d, 8)
	fmt.Printf("d after append: %p\n", &d)
	pri()
}

func pri() {
	ch := make(chan int, 10)
	ch <- 10
	// <-ch
	// fmt.Println('完成')
	fmt.Println("完成")
}

/*
a: 5, 5
b: 2, 7
c: 1, 6
d: 4, 7 内存地址不变


报单引号使用错误
修复单引号后也会报错，报无缓冲区chan因只有写入而没有消费导致的deadlock, 修复可通过加缓冲区或者消费此chan信息或删除chan使用代码

select (case when post_like.user_id = 1 then 0 else 1 end) as flag, post.id, post_like.user_id from post left join post_like on post.id = post_like.post_id order by flag;
*/
