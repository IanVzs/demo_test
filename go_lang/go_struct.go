package main

import (
	"fmt"
	"strconv"
)

type Books struct {
	title string
	page  int
}

func (b *Books) get_all() string {
	msg := b.title + "_" + strconv.Itoa(b.page)
	return msg
}

func print_detail(book_path *Books) {
	book := *book_path
	book.page++
	book_path.page++
	// 指针传入, 可修改原内容
	fmt.Println(book.title, "'s page is:", book.page)
}

func print_detail2(book Books) {
	book.page++
	fmt.Println(book.title, "'s page is:", book.page)
}

func main() {
	var book2 = Books{title: "Hello, Golang", page: 123}
	book1 := Books{"Hi, Golang", 521}
	fmt.Println(book1)
	print_detail2(book2)
	fmt.Println(book2)
	print_detail(&book2)
	fmt.Println(book2)
	fmt.Println("Books func: ", book2.get_all())
}
