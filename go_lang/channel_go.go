package main

import (
	"fmt"
	"math/rand"
	"time"
)

func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	done <- true
}

type Msg struct {
	ID        string
	ObjectMap map[string]string
}

func getMessgaeGroup(id string) []string {
	return []string{"1", "2", "3"}
}

type AmnesiaMap struct {
	Map map[string]time.Time
}

func (self AmnesiaMap) Get(id string) bool {
	v, ok := self.Map[id]
	if !ok {
		fmt.Println("Get None Ret false")
	} else {
		td := time.Now().Sub(v)
		fmt.Printf("self.Map:  %+v,  Time Sub: %f\n", self.Map, td.Seconds())
		if td.Seconds() < 30 {
			fmt.Println("Less 30 Ret true")
			return true
		}
	}
	fmt.Println("AmnesiaMap Get true")
	return false
}

func (self *AmnesiaMap) Set(id string) bool {
	if len(self.Map) == 0 {
		self.Map = make(map[string]time.Time)
	}
	v, ok := self.Map[id]
	signUpdate := false
	if !ok {
		signUpdate = true
	} else {
		td := time.Now().Sub(v)
		if td.Seconds() > 30 {
			self.Map[id] = time.Now()
			fmt.Println("Reset when more 30s")
			signUpdate = true
		}
	}
	if signUpdate {
		self.Map[id] = time.Now()
		fmt.Println("Set AmnesiaMap: ", self.Map)
	}
	return signUpdate
}

// 慢慢的说
func talkSlowly(msg Msg) {
	slp := false
	listMsg := getMessgaeGroup(msg.ID)
	for _, v := range listMsg {
		if slp {
			// 第一句话无需延迟
			time.Sleep(time.Second * 1)
		}
		fmt.Println("Let me say: ", v)
		slp = true
	}
}

func talk(message chan Msg) {
	anbesiaNap := AmnesiaMap{}
	for {
		msg := <-message
		fmt.Printf("Get Msg: %+v\n", msg)

		if anbesiaNap.Get(msg.ID) {

		} else {
			if anbesiaNap.Set(msg.ID) {
				go talkSlowly(msg)
			}
		}
		time.Sleep(time.Second * 1)
	}
}

func collect(message chan Msg) {
	m := make(map[string]string)
	m["123"] = "abc"

	wd := "👋"
	if rand.Intn(10) >= 5 {
		wd = "🐶"
	}
	message <- Msg{ID: wd, ObjectMap: m}
}

func main() {

	// done := make(chan bool, 1)
	// go worker(done)

	// <-done

	message := make(chan Msg, 20)
	go talk(message)
	for {
		collect(message)
	}
}
