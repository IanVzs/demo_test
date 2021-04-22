package main

import (
	"fmt"
	"strings"
)

func main() {
	// var hello string = "i am a Clanger"
	listToken := strings.Split("'50989718997307392_._123_._1_._5fa769c142e6df8c6a36b3d3'", "_._")

	if listToken[0][0] == '\'' {
		listToken[0] = listToken[0][1:]
	}
	lenList := len(listToken) - 1
	lenItem := len(listToken[lenList]) - 1
	if listToken[lenList][lenItem] == '\'' {
		listToken[lenList] = listToken[lenList][:lenItem]
	}
	fmt.Println(listToken[0], listToken[1], listToken[2], listToken[3])
}
