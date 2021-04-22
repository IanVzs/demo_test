package soi

import (
	"encoding/json"
	"log"
	"net/http"

	"ianvzs.io/http_server/rds"
)

type UpDetails struct {
	Name   string `json:"name"`
	Update int    `json:"update"`
}
type AlertResp struct {
	Code           string      `json:"code"`
	Status         int         `json:"status"`
	Msg            string      `json:"msg"`
	Update         int         `json:"update"`
	Update_details []UpDetails `json:"update_details"`
}

type GenKey struct {
	ChatId string
	Uid    string
	Action string
}

func (keys *GenKey) getKeyUid() string {
	return keys.Action + keys.ChatId + keys.Uid
}
func (keys *GenKey) getKeyNoUid() string {
	return keys.Action + keys.ChatId
}

// http Api:获取soi_chat提醒
func SoiAlert(w http.ResponseWriter, req *http.Request) {
	var rst AlertResp
	req.ParseForm()
	chat_id, cErr := req.Form["chat_id"]
	uid, uErr := req.Form["uid"]
	action, aErr := req.Form["action"]
	if !cErr && !uErr {
		log.Println("!cErr && !uErr")
		rst = AlertResp{"200", 1, "请求失败", 0, []UpDetails{}}
	} else if !aErr {
		log.Println("!aErr")
		rst = AlertResp{"200", 0, "请求成功", 0, []UpDetails{}}
	} else {
		log.Println(action[0])
		genkey := GenKey{ChatId: chat_id[0], Uid: uid[0], Action: action[0]}
		key := genkey.getKeyUid()
		update := rds.ExampleClient(key)
		rst = AlertResp{"200", 0, "请求成功", update, []UpDetails{}}
	}

	log.Println("Get rst from rds: ", rst)
	if err := json.NewEncoder(w).Encode(rst); err != nil {
		log.Fatal(err)
	}
	// for name, headers := range req.Header {
	// 	for _, h := range headers {
	// 		fmt.Fprintf(w, "%v: %v\n", name, h)
	// 	}
	// }
}
