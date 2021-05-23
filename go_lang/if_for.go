package main

/**
## go的循环
- golang 只有for  while==for
- golang 中没有小括号包裹, 只需要用{}分隔作用域就可以

for 可以有
1. for A;B;C {}
2. for ;B; {}
3. for {}

## go的switch
- 每个case自动break
- fallthrough 显式声明可以继续执行下一个case
- case 无需常量
- `switch {case}` 可做 if-else 用
**/
import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	// v在这儿/{}之外, 作用范围也只在{内这个作用域中.}
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
