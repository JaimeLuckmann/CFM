jQuery(document).ready(function($) {

    $squares = document.querySelectorAll('a.btn.pop')

    $squares.forEach(e => {
        // console.log($square);
        position = parseFloat(document.defaultView.getComputedStyle(e)["top"]);
        // console.log(document.defaultView.getComputedStyle(e)["top"]);
        if (position>145) {
            $popupContent = e.children[0];
            console.log($popupContent);
            $popupContent.classList.toggle("arriba");
        }
    });

    $body = document.body;
    $body.addEventListener('click',function(event){
        $elementoClickeado = event.target;

        $myPopups = $('[id="myPopup"]');

        // Se abre y se cierra sólo al apretar el square
        if ($elementoClickeado.id=="aPopUp") {
            

            // Si hay algún popup abierto distinto, lo cierra
            $myPopups.each(function(){
            $popup = this;
            if ( ($popup.classList[1] == "show"  || $popup.classList[2] == "show") 
            &&  event.path[0].children[0] != $popup) {                            
                $popup.classList.toggle("show");
                }
            })

            // Abre el popup seleccionado.
            $square = event.path[0];
            var $popup = $square.children[0]    
            $popup.classList.toggle("show");
            
            // Intento de cambiar el square de color cuando se le presiona. No funcionó.
            $popup.parentElement.style.border = "2.5px solid red!important;"

        }
        else{
            
            // Al apretar fuera de los popup se cierran
            $myPopups.each(function(){
                $popup = this;
                if (($popup.classList[1] == "show"  || $popup.classList[2] == "show") ) {  
                    if ($elementoClickeado.id != "myPopup") {

                        $popup.classList.toggle("show");
                    }
                }
            })

        }
    })


  })