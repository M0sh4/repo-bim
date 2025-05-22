import qa from './qa.js';

const map = {
  QA: qa
};

const env = __ENV.ENV;     // lee ENV desde la CLI
const cfg = map[env];

export const API_ENDPOINTS = cfg.API_ENDPOINTS;
export const RESOURCES     = cfg.RESOURCES;
export const API_KEY       = cfg.API_KEY;
export const AES = cfg.AES
export default cfg;
