//formularios
//formulario del register
document.getElementById("valPassword").style.display = "none";
document.getElementById("valNombre").style.display = "none";
document.getElementById("valUsuario").style.display = "none";
document.getElementById("valCorreo").style.display = "none";

function validar(){
    if (document.getElementById("txtUsuario").value.length == 0) {
        document.getElementById("valUsuario").style.display = "inline";
        document.getElementById("txtUsuario").classList.add("is-invalid");
    }else{
        document.getElementById("valUsuario").style.display = "none";
        document.getElementById("txtUsuario").classList.remove("is-invalid");
        document.getElementById("txtUsuario").classList.add("is-valid");
    }
    if (document.getElementById("txtNombre").value.length == 0) {
        document.getElementById("valNombre").style.display = "inline";
        document.getElementById("txtNombre").classList.add("is-invalid");
    }else{
        document.getElementById("valNombre").style.display = "none";
        document.getElementById("txtNombre").classList.remove("is-invalid");
        document.getElementById("txtNombre").classList.add("is-valid");
    }
    if (document.getElementById("txtPassword").value.length == 0) {
        document.getElementById("valPassword").style.display = "inline";
        document.getElementById("txtPassword").classList.add("is-invalid");
    }else{
        document.getElementById("valPassword").style.display = "none";
        document.getElementById("txtPassword").classList.remove("is-invalid");
        document.getElementById("txtPassword").classList.add("is-valid");
    }
    if (document.getElementById("emailCorreo").value.length == 0) {
        document.getElementById("valCorreo").style.display = "inline";
        document.getElementById("emailCorreo").classList.add("is-invalid");
    }else{
        document.getElementById("valCorreo").style.display = "none";
        document.getElementById("emailCorreo").classList.remove("is-invalid");
        document.getElementById("emailCorreo").classList.add("is-valid");
    }
}

document.getElementById("ocultar").style.display = "none";

function pass(){
    let input = document.getElementById("txtPassword");

    if (input.type == "password") {
        input.type = "text";
        document.getElementById("ocultar").style.display = "inline";
        document.getElementById("mostrar").style.display = "none";
    }else{
        input.type = "password";
        document.getElementById("ocultar").style.display = "none";
        document.getElementById("mostrar").style.display = "inline";
    }


}

//formulario del Login
//falta

document.getElementById("valPass").style.display = "none";
document.getElementById("valUser").style.display = "none";

function validarLog(){
    if (document.getElementById("txtPass").value.length == 0) {
        document.getElementById("valPass").style.display = "inline";
        document.getElementById("txtPass").classList.add("is-invalid");
    }else{
        document.getElementById("valPass").style.display = "none";
        document.getElementById("txtPass").classList.remove("is-invalid");
        document.getElementById("txtPass").classList.add("is-valid");
    }
    if (document.getElementById("txtUser").value.length == 0) {
        document.getElementById("valUser").style.display = "inline";
        document.getElementById("txtUser").classList.add("is-invalid");
    }else{
        document.getElementById("valUser").style.display = "none";
        document.getElementById("txtUser").classList.remove("is-invalid");
        document.getElementById("txtUser").classList.add("is-valid");
    }
}
