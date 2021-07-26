package main

import (
	"fmt"

	"golang.org/x/crypto/bcrypt"
)

func main() {
	//密码加密
	hash, err := hashEncode("123456")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("hash过的密码：", hash)

	//密码校验
	sourcePwd := "123456"
	pwdMatch := comparePasswords(hash, sourcePwd)
	if pwdMatch {
		fmt.Println("验证密码成功！")
	} else {
		fmt.Println("验证密码失败！")
	}
}

/*
 * hash 加密密码
 * @param string pwd 待加密的明文密码
 */
func hashEncode(pwd string) (string, error) {
	hash, err := bcrypt.GenerateFromPassword([]byte(pwd), bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}
	return string(hash), nil
}

/*
 * 验证 hash 密码
 * @param string hashedPwd 已加密的hash密码
 * @param string sourcePwd 确认密码
 */
func comparePasswords(hashedPwd string, sourcePwd string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hashedPwd), []byte(sourcePwd))
	if err != nil {
		return false
	}
	return true
}
