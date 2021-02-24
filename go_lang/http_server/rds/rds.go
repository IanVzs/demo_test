package rds

import (
	"fmt"
	"log"
	"strconv"

	"context"

	"github.com/go-redis/redis/v8"
)

var ctx = context.Background()

// ExampleClient: 从redis中获取数值 入参key
func ExampleClient(key string) int {
	rdb := redis.NewClient(&redis.Options{
		Addr:     "192.168.0.202:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})
	// region Demo
	err := rdb.Set(ctx, "key", "1", 0).Err()
	if err != nil {
		panic(err)
	}

	val, err := rdb.Get(ctx, "key").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("key", val)

	val2, err := rdb.Get(ctx, "key2").Result()
	if err == redis.Nil {
		fmt.Println("key2 does not exist")
	} else if err != nil {
		panic(err)
	} else {
		fmt.Println("key2", val2)
	}
	// Output: key value
	// key2 does not exist
	//endregion
	intRst := 0
	rst, err := rdb.Get(ctx, key).Result()
	if err == redis.Nil {
		log.Println("not get ", key)
		rst = "0"
	} else if err != nil {
		panic(err)
	} else {
		intRst, err = strconv.Atoi(rst)
		if err != nil {
			panic(err)
		}
		log.Println("key", intRst)
	}
	return intRst
}
