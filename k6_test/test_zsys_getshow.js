import http from "k6/http"

export default function() {
    //let response = http.get("https://zsys-test.zuoshouyisheng.com/service_setting/get_show");
    let response = http.get("https://www.baidu.com");
}
