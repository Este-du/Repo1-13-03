let btnCarrito = document.getElementById('btnCarrito');

btnCarrito.addEventListener('click', function(){
    arrayStorage = [
        {
            sku:1,
            nombre:'comida',
            precio: 135,
            cantidad: 15
        },
        {
            sku:2,
            nombre:'comida',
            precio: 135,
            cantidad: 13
        },
        {
            sku:3,
            nombre:'comida',
            precio: 135,
            cantidad: 12
        }
    ]

    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    fetch('/carrito',{
        method: 'POST',
        headers:{
            'content-type': 'application/json',
            'X-CSRFToken': token
        },
        body:JSON.stringify(arrayStorage)
    })
})