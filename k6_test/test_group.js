import { group, check } from 'k6';
import http from 'k6/http';

export default function () {
    // reconsider this type of code
    var id = 123;
    group('get post', function () {
       http.get(`http://example.com/posts/${id}`);
    });
    group('list posts', function () {
       let res = http.get(`http://example.com/posts`);
       check(res, {
         'is status 200': (r) => r.status === 200,
       });
    });
}   
