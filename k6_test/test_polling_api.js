import { check } from 'k6';
import http from "k6/http"

export default function() {
    // let response = http.get("http://localhost:8080/soi/polling?uid=123&action=had_msgs");
    let response = http.get("http://211.154.163.93:6157/pharm_api/soi_chat/polling?uid=123&action=had_msgs&chat_id=42629189186621440&auth_code=1qdwqdq");
    check(response, {'is status 200': (r) => r.status === 200,
    });
}
