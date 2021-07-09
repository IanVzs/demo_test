package gredis

import (
	"encoding/json"
	"errors"
	"fmt"
	"time"

	"github.com/gomodule/redigo/redis"
)

var RedisConn *redis.Pool

// Setup Initialize the Redis instance
func Setup() error {
	fmt.Println("\nRedis Config: ", Redis)
	RedisConn = &redis.Pool{
		MaxIdle:     Redis.Maxidle,
		MaxActive:   Redis.Maxactive,
		IdleTimeout: time.Duration(Redis.Idletimeout),
		Dial: func() (redis.Conn, error) {
			c, err := redis.Dial("tcp", Redis.Host)
			if err != nil {
				return nil, err
			}
			if Redis.Password != "" {
				if _, err := c.Do("AUTH", Redis.Password); err != nil {
					c.Close()
					return nil, err
				}
			}
			return c, err
		},
		TestOnBorrow: func(c redis.Conn, t time.Time) error {
			_, err := c.Do("PING")
			return err
		},
	}
	return nil
}

// Set a key-field/value
func HSet(key string, field string, data interface{}) error {
	conn := RedisConn.Get()
	defer conn.Close()

	value, err := json.Marshal(data)
	if err != nil {
		return err
	}

	_, err = conn.Do("HSET", key, field, value)
	if err != nil {
		return err
	}

	return nil
}

// Get get a key
func HGet(key string, field string) ([]byte, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	reply, err := redis.Bytes(conn.Do("HGET", key, field))
	if err != nil {
		return nil, err
	}

	return reply, nil
}

// HDel Del a field in key
func HDel(key string, field string) (bool, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	signDel, err := redis.Bool(conn.Do("HDEL", key, field))
	if err != nil {
		return signDel, err
	}

	return signDel, nil
}

// HKeys Get all fields in A hash key
func HKeys(key string) ([]string, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	listKeys := []string{}
	reply, err := redis.Values(conn.Do("HKEYS", key))
	if err != nil {
		return nil, err
	}
	for _, v := range reply {
		if vv, ok := v.([]byte); ok {
			listKeys = append(listKeys, string(vv))
		} else {
			return nil, errors.New("decode hkeys error")
		}
	}
	return listKeys, nil
}

// Set a key/value
func Set(key string, data interface{}, time int) error {
	conn := RedisConn.Get()
	defer conn.Close()

	value, err := json.Marshal(data)
	if err != nil {
		return err
	}

	_, err = conn.Do("SET", key, value)
	if err != nil {
		return err
	}

	_, err = conn.Do("EXPIRE", key, time)
	if err != nil {
		return err
	}

	return nil
}

// Exists check a key
func Exists(key string) bool {
	conn := RedisConn.Get()
	defer conn.Close()

	exists, err := redis.Bool(conn.Do("EXISTS", key))
	if err != nil {
		return false
	}

	return exists
}

// Get get a key
func Get(key string) ([]byte, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	reply, err := redis.Bytes(conn.Do("GET", key))
	if err != nil {
		return nil, err
	}

	return reply, nil
}

// Delete delete a kye
func Delete(key string) (bool, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	return redis.Bool(conn.Do("DEL", key))
}

// LikeDeletes batch delete
func LikeDeletes(key string) error {
	conn := RedisConn.Get()
	defer conn.Close()

	keys, err := redis.Strings(conn.Do("KEYS", "*"+key+"*"))
	if err != nil {
		return err
	}

	for _, key := range keys {
		_, err = Delete(key)
		if err != nil {
			return err
		}
	}

	return nil
}

// lpush
// queue name: qName
// keys 每个元素里请包含serverID信息
func QLpush(qName string, keys []string) error {
	conn := RedisConn.Get()
	defer conn.Close()

	_, err := conn.Do("lpush", redis.Args{}.Add(qName).AddFlat(keys)...)
	return err
}

// pop
// queue name: qName
// ret Data中会有serverID信息 注意区分处理
func QPop(qName string, timeout int) (string, error) {
	conn := RedisConn.Get()
	defer conn.Close()

	nameAndData, err := redis.Strings(conn.Do("brpop", qName, timeout))
	if err != nil {
		return "", err
	}
	if len(nameAndData) > 1 {
		resData := nameAndData[1]
		return resData, nil
	}

	return "", nil
}

