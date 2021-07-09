package gredis

type RedisCfg struct {
    Maxidle int
    Maxactive int
    Idletimeout int
    Host string
    Password string
}
var (
    Redis = RedisCfg{30, 30, 200, "127.0.0.1:6379", ""}
)
