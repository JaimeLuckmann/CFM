
jQuery(document).ready(function($) {

    $body = document.body;
    $body.addEventListener('click',function(event){

        $elementoClickeado = event.target;

        // Los siguientes condicionales se encargan de abrir y cerrar el carrito.

        // muestra el carrito al apretar el icono del carrito de compra
        if ($elementoClickeado.id == "carrito"){
            document.getElementById("listaCarrito").classList.toggle("show");

        }

        // cierra el carrito apretando el icono de la x.
        if ($elementoClickeado.id == "cerrar"){
            // cambia la visibilidad del carrito a oculto con efecto de fadeout.
            document.getElementById("listaCarrito").style.visibility = "visible";
            document.getElementById("listaCarrito").classList.toggle("show");
            // setTimeout de 0.5 seg para sincronizarse con efecto fadeout en css.
            setTimeout(function(){
            document.getElementById("listaCarrito").style.visibility = "hidden";
            },500)
            
        }                

        // Este fue el avance tratando de agregar botones de eliminar filas...
        if ($elementoClickeado.id.slice(0,6) == "delete"){
            $productoEliminar = $elementoClickeado.id.slice(7);
            fetch("static/json/carrito/carrito.json")
                .then(function(resp){
                    return resp.json();
                })
                .then(function($carrito){
                    delete $carrito[$productoEliminar];
                    $carritoJSON = JSON.stringify($carrito);
                    console.log(typeof $carritoJSON);
                    
                })

        }
        


    })

})