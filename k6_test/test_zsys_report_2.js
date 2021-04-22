import { check } from 'k6';
import http from 'k6/http';

export default function () {
  var url = 'https://zsys-test.zuoshouyisheng.com/presc/audit_report_id';
  var payload = '{"auth_code": "1447a54e84f9416d92fdfebd592028af", "user_id": "user_id", "user_info": {"age": "0岁", "gender": "男", "name": "银川测试", "department": "内科", "diagnosis": ["感冒"]}, "user_docs": [{"name": "银川测试", "gender": "男", "age": "0岁", "department": "内科", "diagnosis": ["感冒"], "prescription": [{"generic_name": "阿莫西林克拉维酸钾咀嚼片(8:1)", "size": "281.25mg*10片", "countIndex": [0, 0], "order_quality": 1, "order_unit": "盒", "courseIndex": "6", "course": "7天", "showDosPicker": false, "deliveryValue": 0, "delivery": "口服", "deliveryIndex": 0, "showPicker": false, "single_dose": "3", "single_unit": "片", "frenValues": [[2, 0], [2, 0]], "showFrePicker": false, "frequency": "2次/1天"}], "supplement": ""}]}';

  var params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  
  let res = http.post(url, payload, params);
  check(res, {
      "is status 200": (r) => r.status === 200,
  });
}
