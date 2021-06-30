package utils

import (
	"fmt"
	"time"
)

var (
	AmnesiaMapObject = AmnesiaMap{}
)

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
