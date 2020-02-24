package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	b := []byte(`{"Title":"Go语言编程","Authors":["XuShiwei","HughLv","Pandaman","GuaguaSong","HanTuo","BertYuan","XuDaoli"],"Publisher":"ituring.com.cn","IsPublished":true,"Price":9.99,"Sales":1000000, "mutil": {"go": "yes?"}}`)
	var r interface{}
	err := json.Unmarshal(b, &r)
	if err == nil {
		fmt.Println(r)
	}

	gobook, ok := r.(map[string]interface{})
	if ok {
		for k, v := range gobook {
			switch v2 := v.(type) {
			case string:
				fmt.Println(k, "is string", v2)
			case int:
				fmt.Println(k, "is int", v2)
			case bool:
				fmt.Println(k, "is bool", v2)
			case []interface{}:
				fmt.Println(k, "is an array:")
				for i, iv := range v2 {
					fmt.Println(i, iv)
				}
			default:
				fmt.Println(k, "is another type not handle yet")
			}
		}
	}
}
