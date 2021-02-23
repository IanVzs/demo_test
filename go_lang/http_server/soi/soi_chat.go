package soi

import (
	"fmt"
	"net/http"
)

// http Api:获取soi_chat提醒
func SoiAlert(w http.ResponseWriter, req *http.Request) {
	for name, headers := range req.Header {
		for _, h := range headers {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}
