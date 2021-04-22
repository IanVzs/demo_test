import http from 'k6/http';
import { check } from 'k6';

export default function () {
  var url = 'http://test.k6.io/login';
  var payload = JSON.stringify({
    email: 'aaa',
    password: 'bbb',
  });

  var params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  let res = http.post(url, payload, params);

  check(res, {
      "is status 404": (r) => r.status === 404,
  });
}
