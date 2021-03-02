import { check } from 'k6';
import http from "k6/http"

export default function() {
    let response = http.get("http://localhost:8080/soi/polling?uid=123&action=had_msgs");
    check(response, {'is status 200': (r) => r.status === 200,
    });
}
