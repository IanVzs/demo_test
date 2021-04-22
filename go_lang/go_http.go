package main

import (
    "bufio"
    "fmt"
    "net/http"
    "io/ioutil"
    "encoding/json"
)


type RssListItem struct{
    Url string `json:"url"`
    Description string `json:"description"`
    Srtdesc string `json:"srtdesc"`
    Articles []string `json:"articles"`
}

func get() {

    resp, err := http.Get("http://127.0.0.1:5481/rss/?skip=0&limit=100")
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("Response status:", resp.Status)

    body, _ := ioutil.ReadAll(resp.Body)

    // region 解析byte2JSON
    var res []RssListItem
    err = json.Unmarshal(body, &res)
    if err == nil {
        fmt.Println(res)
    }
    //endregion

    // region 获取列表元素
    lenRes := len(res)
    for i:=0; i<lenRes; i++{
        fmt.Println(res[i].Url)
        fmt.Println(res[i].Description)
    }
    //endregion

    // region 错误获取法
    for k,v := range res{
        fmt.Println(k, ":", v)
    }
    //endregion

    // region 打印结构体方法
    fmt.Printf("\n\n有kv:")
    fmt.Printf("%+v\n", res[0])
    //endregion

}

func get_example() {

    resp, err := http.Get("http://gobyexample.com")
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("Response status:", resp.Status)

    scanner := bufio.NewScanner(resp.Body)
    for i := 0; scanner.Scan() && i < 7; i++ {
        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        panic(err)
    }
}

func main() {
    get()
}
