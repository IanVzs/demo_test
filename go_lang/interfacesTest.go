package main

import (
	"fmt"
)

// region 修改属性
type fruit interface{
    getName() string
    setName(name string)
}
type apple struct{
    name string
}
//[1]
func (a *apple) getName() string{
    return a.name
}
//[2]
func (a *apple) setName(name string) {
   a.name = name
}
func testInterface(){
    a:=apple{"红富士"}
    fmt.Println(a.getName())
    a.setName("树顶红")
    fmt.Println(a.getName())
}

//endregion

// region 一般用法+当作参数
type Phone interface {
    call() string
}

type Android struct {
    brand string
}

type IPhone struct {
    version string
}

func (android Android) call() string {
    return "I am Android " + android.brand
}

func (iPhone IPhone) call() string {
    return "I am iPhone " + iPhone.version
}

func printCall(p Phone) {
    fmt.Println(p.call() + ", I can call you!")
}

func testInterfaceAsParams() {
    var vivo = Android{brand:"Vivo"}
    var hw = Android{"HuaWei"}

    i7 := IPhone{"7 Plus"}
    ix := IPhone{"X"}

    printCall(vivo)
    printCall(hw)
    printCall(i7)
    printCall(ix)
}
//endregion




func main() {
	testInterface()
	testInterfaceAsParams()
}
