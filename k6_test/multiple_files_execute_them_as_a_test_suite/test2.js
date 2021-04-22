import http from "k6/http";
import { sleep, check } from "k6";

export default function() {
  let res = http.get("http://something-else.example.com");
  sleep(1);

  check(res, {
      "status is 200": (r) => r.status === 200,
      "response body": (r) => r.body.indexOf("Im something completely different")
  });
}
