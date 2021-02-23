package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"

	"ianvzs.io/http_server/soi"
)

var addr = flag.String("addr", ":8080", "http service address")

func hello(w http.ResponseWriter, r *http.Request) {
	log.Println(r.URL)
	if r.URL.Path != "/" {
		http.Error(w, "Not found", http.StatusNotFound)
		return
	}
	if r.Method != "GET" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	// http.ServeFile(w, r, "home.html")
	fmt.Fprintf(w, "hello\n")
}

func main() {
	flag.Parse()
	http.HandleFunc("/", hello)
	http.HandleFunc("/headers", soi.SoiAlert)
	log.Printf("server run: " + *addr)
	err := http.ListenAndServe(*addr, nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
