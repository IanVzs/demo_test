package main

import (
	"fmt"
	"sort"
)

func in(target string, str_array []string) bool {
	sort.Strings(str_array)
	index := sort.SearchStrings(str_array, target)

	if index < len(str_array) && str_array[index] == target {
		return true
	}
	return false
}

func main() {
	ok := in("hello", []string{"hi", "hello", "hey"})
	fmt.Println("hello in ?  ", ok)

	ok = in("hello2", []string{"hi", "hello", "hey"})
	fmt.Println("hello2 in ?  ", ok)

	ok = in("hi", []string{"hi", "hello", "hey"})
	fmt.Println("hi in ?  ", ok)

	ok = in("he", []string{"hi", "hello", "hey"})
	fmt.Println("he in ?  ", ok)

	ok = in("hey", []string{"hi", "hello", "hey"})
	fmt.Println("hey in ?  ", ok)
}
