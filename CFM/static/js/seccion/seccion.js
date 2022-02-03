function pagina(num){

    $contenedores = document.getElementsByClassName("contenedor-secciones")

    for($contenedor of $contenedores){

        //Esconde la página activa.
        if ($contenedor.classList[1] != "hidden" && parseFloat($contenedor.id)!=num) {
            $contenedor.classList.toggle("hidden")
            $liPag = document.getElementById("pagina".concat($contenedor.id))
            $liPag.classList.toggle("active")
        }

        //Aparece la página seleccionada.
        if($contenedor.classList[1] == "hidden" && parseFloat($contenedor.id)==num){
            $contenedor.classList.toggle("hidden")
            $liPag = document.getElementById("pagina".concat($contenedor.id))
            $liPag.classList.toggle("active")
            disabled(parseFloat($contenedor.id))
        }
    }
}

function siguiente(){

    $contenedores = document.getElementsByClassName("contenedor-secciones")
    num_contenedores = $contenedores.length

    for($contenedor of $contenedores){

        if($contenedor.classList[1] != "hidden"){
            num = parseFloat($contenedor.id)
            
            if(num < num_contenedores){
                pagina(num+1);
                break;
            }
        }
    }
}

function anterior(){

    $contenedores = document.getElementsByClassName("contenedor-secciones")
    num_contenedores = $contenedores.length

    for($contenedor of $contenedores){

        if($contenedor.classList[1] != "hidden"){
            num = parseFloat($contenedor.id)
            
            if(num > 1){

                pagina(num-1);
                break;
            }
        }
    }
}


function disabled(num){
    $anterior = document.getElementById("anterior")
    $siguiente = document.getElementById("siguiente")

    if(num>1 && $anterior.classList[1]=="disabled"){
        $anterior.classList.toggle("disabled")
    }

    if(num==1 && $anterior.classList[1]!="disabled"){
        $anterior.classList.toggle("disabled")
    }

    $contenedores = document.getElementsByClassName("contenedor-secciones")
    num_contenedores = $contenedores.length

    if(num<num_contenedores && $siguiente.classList[1]=="disabled"){
        $siguiente.classList.toggle("disabled")
    }

    if(num==num_contenedores && $siguiente.classList[1]!="disabled"){
        $siguiente.classList.toggle("disabled")
    }

}

