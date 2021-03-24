package main

import (
	"fmt"
	"encoding/json"
)


func main() {
	var jsonBlob = []byte(`[
		{"Name": "Platypus", "Order": "Monotremata"},
		{"Name": "Quoll",    "Order": "Dasyuromorphia"}
	]`)
	type Animal struct {
		Name  string
		Order string
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v\n", animals)

    showSingleString := func () {
        var ss string
        ss = "1234567890"
        s, err := json.Marshal(ss)
        if err != nil {
            fmt.Println("Marshal err", err)
        }
        fmt.Println(s)
        fmt.Println(string(s))
        // 转换出的字符串首尾有双引号("")...
    }
    showSingleString()
    showSingleString2 := func () {
        s := "\"1234567890\""
        var ss string
        json.Unmarshal([]byte(s), &ss)
        fmt.Println(ss)
    }
    showSingleString2()
}
