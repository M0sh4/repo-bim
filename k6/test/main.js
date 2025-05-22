import login from './requests/login.js';

export const options = {
  vus: 1,
  duration: '1s',
};

export default async function () {
  await login()
}