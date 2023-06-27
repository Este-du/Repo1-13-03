console.log("js desde Django");
const formulario = document.getElementById("formularioAgregarProducto")

formulario.addEventListener('submit', function(evnto){
    evento.preventDefault();

    if (document.getElementById('txtSku').value.length == 0){
        alert("debe ingresar el codigo del producto")
        return;
    }else{
        this.submit();
    }
})