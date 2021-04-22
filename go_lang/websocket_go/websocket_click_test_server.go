package main

import (
	"flag"
	"fmt"
	"net/url"
	"time"

	"github.com/gorilla/websocket"
)

var addr = flag.String("addr", "127.0.0.1:8000", "http service address")
var msg = flag.String("msg", "time", "this client send msg.")
var id = flag.String("id", "123", "join this chat room.")

func init() {
	flag.Parse()
}

func main() {
	// go mainWsEcho()
	mainWsChat()
}

func mainWsChat() {
	u := url.URL{Scheme: "ws", Host: *addr, Path: "/ws_chat", RawQuery: "chat_id=" + *id}
	// u := url.URL{Scheme: "ws", Host: *addr, Path: "/ws_chat"}
	var dialer *websocket.Dialer

	conn, _, err := dialer.Dial(u.String(), nil)
	if err != nil {
		fmt.Println(err)
		return
	}

	go timeWriter(conn)

	for {
		_, message, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("read:", err)
			return
		}

		fmt.Printf("received: %s\n", message)
	}
}

func mainWsEcho() {
	// u := url.URL{Scheme: "ws", Host: *addr, Path: "/ws"}
	u := url.URL{Scheme: "ws", Host: *addr, Path: "/ws"}
	var dialer *websocket.Dialer

	conn, _, err := dialer.Dial(u.String(), nil)
	if err != nil {
		fmt.Println(err)
		return
	}

	go timeWriter(conn)

	for {
		_, message, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("read:", err)
			return
		}

		fmt.Printf("received: %s\n", message)
	}
}

func timeWriter(conn *websocket.Conn) {
	for {
		time.Sleep(time.Second * 1)
		// time.Sleep(time.Microsecond * 1)
		sendMsg := *msg
		if sendMsg == "time" {
			conn.WriteMessage(websocket.TextMessage, []byte(time.Now().Format("2006-01-02 15:04:05")))
		} else {
			conn.WriteMessage(websocket.TextMessage, []byte(sendMsg))
		}

	}
}
