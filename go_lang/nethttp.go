package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	type PostData struct {
		Appid string //`json:"appid"`
	}
	pull_data := PostData{Appid: "5c99b1a09ea2ea68c824dad8"}
	pull_buff := new(bytes.Buffer)
	json.NewEncoder(pull_buff).Encode(pull_data)
	var url string = "http://129.28.192.11:8979/testapi"
	// var url string = "http://129.28.192.11:8979/testapi"
	var url string = "http://httpbin.org/post"
	//res, err := http.Post("https://zsys.zuoshouyisheng.com/service_setting/pull", "application/json; charset=utf-8", pull_buff)
	req, err := http.NewRequest("POST", url, pull_buff)
	req.Header.Set("Content-Type", "application/json")
	client := &http.Client{}
	res, err := client.Do(req)

	//res, err := http.Get("https://wx.zuoshouyisheng.com/wx_api/get_menu?app_id=wxa5176049e943f3b5")
	if err != nil {
		log.Fatal(err)
	}
	robots, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", robots)
}
