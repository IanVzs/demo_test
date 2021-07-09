/**
Warning:
	使用到了
		1, test
	这两个Key

	运行后会删除
**/
package tests

import (
	"encoding/json"
	"testing"

)

type Data struct {
	A string
}

func TestHset(t *testing.T) {
	err := config.LoadConfig()
	if err != nil {
		panic("!!!????????")
	}
	gredis.Setup()
	/********region Set Get********/
	err = gredis.Set("test", Data{A: "hello"}, 10)
	if err != nil {
		t.Log(err)
	}

	bdata, err := gredis.Get("test")
	hi := Data{}
	err = json.Unmarshal(bdata, &hi)
	t.Logf("获取Redis 值为： %+v", hi)
	/******** endregion ********/

	/********region HSet HGet********/
	err = gredis.HSet("1", "test", Data{A: "hello"})
	err = gredis.HSet("1", "test_2", Data{A: "hello"})
	if err != nil {
		t.Log(err)
	}

	bdata, err = gredis.HGet("1", "test")
	hey := Data{}
	err = json.Unmarshal(bdata, &hey)
	t.Logf("获取Redis HGet 值为： %+v", hey)
	/******** endregion ********/

	/******** region HKeys ********/
	keys, err := gredis.HKeys("1")
	if err != nil {
		t.Log("HKeys 获取失败: ", err)
	}
	t.Logf("获取Redis HKeys 值为： %s", keys)
	/******** endregion ********/

	/*** region Del ***/
	ok, _ := gredis.Delete("1")
	if ok {
		t.Log("成功删除 1")
	}
	ok, _ = gredis.Delete("test")
	ok, _ = gredis.Delete("test_2")
	if ok {
		t.Log("成功删除 test")
	}
	/******** endregion ********/
}

