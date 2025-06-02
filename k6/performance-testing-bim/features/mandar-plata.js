import login from "../scripts/login.js"
import listarFavoritos from "../scripts/listar-favoritos-p2p.js"
import validarUsuario from "../scripts/validar-usuario-p2p.js"
/**
 * Ejecute la función de prueba, Una vez por iteración, tantas veces como lo requieran las opciones de prueba
 */
export default function(users) {
    let tokenLogin = login(users);
    let tokenFav = listarFavoritos(users, tokenLogin);
    validarUsuario(users, tokenFav)
};