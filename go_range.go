package main

import "fmt"

func main() {
	var nums = []int{2, 3, 4}
	var sum int = 0

	//var kvs = map[string]string{'a': "apple", 'b': "ball"}
	var kvs = map[string]string{"a": "apple", "b": "ball"}

	var hello string = "i am a Clanger"

	for _, num := range nums {
		// fmt.Println(_n)
		// fmt.Println(_) 报错哒, 因为'_'为占位, 不可作为value
		sum += num
	}
	fmt.Println("sum: ", sum)
	for _k, _v := range kvs {
		fmt.Printf("%s -> %s\n", _k, _v)
	}
	for i, s := range hello {
		fmt.Printf("%d -> %T|", i, s)
		fmt.Printf("%d -> %d|", i, s)
		fmt.Printf("%s -> %s\n", i, s)
		fmt.Println(i, s)
	}
}
