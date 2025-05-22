import login from './scripts/login.js';
import { read_data } from './utils/read_data.js'
import { SharedArray } from 'k6/data';

/**
 * init context -> es lo primero que se ejecuta, se ejecuta una vez por VU, en el caso de sharedarray se ejecuta solo una vez.
 */
const users = new SharedArray('users', () => {
  const users_path = import.meta.resolve('./../performance-testing-bim/data/users.csv');
  return read_data(users_path,'users');
});


export const options = {
  vus: 1,
  // duration: '1s',
  iterations: 1
};
/**
 * Setup context -> Configurar datos para su procesamiento, compartir datos entre VU, se ejecuta solo una vez.
 */
// export function setup() {

// }

/**
 * VU code -> Ejecute la función de prueba, Una vez por iteración, tantas veces como lo requieran las opciones de prueba
 */
export default function () {
  login(users)
}

/**
 * Teardown -> Resultado del proceso del código de configuración, detener el entorno de prueba, se ejecuta una vez cuando acaba la ejecucion.
 */

// export function teardown(data) {
//   
// }