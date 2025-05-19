// stress-test.js
import { sleep, check } from 'k6';
import http from 'k6/http';

export default () => {
  const res = http.get('https://quickpizza.grafana.com');
  check(res, {
    'status is 200': () => res.status === 200,
  });
  sleep(1);
};