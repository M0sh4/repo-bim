// test.js
import stressTest from './requests/stress-test.js';

export const options = {
  vus: 50,
  duration: '10s',
};

export default function () {
  stressTest();
}