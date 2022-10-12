function verusuarios(){
    var listapost;
    var url="/listadousuarios"
    
    fetch(url)
    .then(response=>response.json())
    .then((data)=>{
    listapost=data;    
    var info=""
    
    for(var i=0;i<listapost.length;i++)
    {
        info=info+"<tr'>"
        info=info+"<td>"+listapost[i]['id'] + "</td>"
        info=info+"<td>"+listapost[i]['nombre'] + "</td>"
        info=info+"<td>"+listapost[i]['apellido'] + "</td>"
        info=info+"<td>"+listapost[i]['email'] + "</td>"
        info=info+"<td>"+listapost[i]['nombre_rol']+ "</td>"
        info=info+"<td> <span class='badge bg-success'>Editar</span> <span class='badge bg-danger'>Eliminar</span></td>"
        info=info+"</tr>"
    
    }
    
 
    document.getElementById("listado").innerHTML=info
    }
    )
    
    }
    
    function vermaterias(){
        var listapost;
        var url="/listadomaterias"
        
        fetch(url)
        .then(response=>response.json())
        .then((data)=>{
        listapost=data;    
        var info=""
        
        for(var i=0;i<listapost.length;i++)
        {
            info=info+"<tr'>"
            info=info+"<td>"+listapost[i]['id_materia'] + "</td>"
            info=info+"<td>"+listapost[i]['nombre_materia'] + "</td>"            
            info=info+"<td> <span class='badge bg-success'>Editar</span> <span class='badge bg-danger'>Eliminar</span></td>"
            info=info+"</tr>"
        
        }
        
     
        document.getElementById("listado").innerHTML=info
        }
        )
        
        }

        function vermatriculados(){
            var listapost;
            var url="/listadomatriculados"
            
            fetch(url)
            .then(response=>response.json())
            .then((data)=>{
            listapost=data;    
            var info=""
            
            for(var i=0;i<listapost.length;i++)
            {
                info=info+"<tr'>"
                info=info+"<td>"+listapost[i]['nombre_materia'] + "</td>"
                info=info+"<td>"+listapost[i]['nombre_rol'] + "</td>"
                info=info+"<td>"+listapost[i]['nombre'] + "</td>" 
                info=info+"<td>"+listapost[i]['apellido'] + "</td>"           
                info=info+"<td><span class='badge bg-danger'>Eliminar</span></td>"
                info=info+"</tr>"
            
            }
            
         
            document.getElementById("listado").innerHTML=info
            }
            )
            
            }

        function veractividad(){
            var listapost;
            identificador =document.getElementById("id_session").innerHTML;    
            console.log(identificador)
            var url="/listaactividad"
            var data = {
                "usuario": identificador                        
        };            
            fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {"Content-type":"application/json;charset=UTF-8"}
                })
            .then(response=>response.json())
            .then((data)=>{
            listapost=data;    
            var info=""
            
            for(var i=0;i<listapost.length;i++)
            {
                info=info+"<tr'>"
                info=info+"<td>"+listapost[i]['id_actividad'] + "</td>"
                info=info+"<td>"+listapost[i]['nombre_actividad'] + "</td>"               
                info=info+"</tr>"
            
            }
            
         
            document.getElementById("listado").innerHTML=info
            }
            )
            
            }
        
            function verpromedio(){
                var listapost;
                identificador =document.getElementById("id_session").innerHTML;    
                console.log(identificador)
                var url="/listapromedio"
                var data = {
                    "usuario": identificador                        
            };            
                fetch(url, {
                method: "POST",
                body: JSON.stringify(data),
                headers: {"Content-type":"application/json;charset=UTF-8"}
                    })
                .then(response=>response.json())
                .then((data)=>{
                listapost=data;    
                var info=""
                
                for(var i=0;i<listapost.length;i++)
                {
                    
                    info=info+"<b>"+'El Promedio General es: '+data+ "</b>"                                  
                    
                
                }
                
             
                document.getElementById("listado2").innerHTML=info
                }
                )
                
                }    
    
        function verpersonal(){
            var listapost;
            identificador =document.getElementById("id_session").innerHTML;
    
            console.log(identificador)
            var url="/listadopersonal";
            var data = {
                        "usuario": identificador                        
                };
    
            fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {"Content-type":"application/json;charset=UTF-8"}
                })
            .then(response=>response.json())
            .then((data)=>{
            listapost=data;    
            var info=""
            
            for(var i=0;i<listapost.length;i++)
            {
                info=info+"<tr class='table-warning'>"
                info=info+"<td>"+listapost[i]['id'] + "</td>"
                info=info+"<td>"+listapost[i]['nombre'] + "</td>" 
                info=info+"<td>"+listapost[i]['apellido'] + "</td>"
                info=info+"<td>"+listapost[i]['email'] + "</td>"
                info=info+"<td>"+listapost[i]['usuario'] + "</td>"
                info=info+"<td>"+listapost[i]['nacimiento'] + "</td>"         
                
                info=info+"</tr>"
            
            }
            
         
            document.getElementById("listado").innerHTML=info
            }
            )
            
            }
            function vernotas(){
                var listapost;
                identificador =document.getElementById("id_session").innerHTML;
        
                console.log(identificador)
                var url="/listanotas";
                var data = {
                            "usuario": identificador                        
                    };
        
                fetch(url, {
                method: "POST",
                body: JSON.stringify(data),
                headers: {"Content-type":"application/json;charset=UTF-8"}
                    })
                .then(response=>response.json())
                .then((data)=>{
                listapost=data;    
                var info=""
                
                for(var i=0;i<listapost.length;i++)
                { 
                    info=info+"<table class='table table-hover'>"
                    info=info+"<tr class='table-dark'>"
                    info=info+"<th colspan='3'>"+listapost[i]['nombre_materia'] +"</th>"
                    info=info+"</tr>"
                    info=info+"<tr class='table-primary'>"
                    info=info+"<th>ACTIVIDADES</th>"
                    info=info+"<th>NOTAS</th>"
                    info=info+"<th>OBSERVACIONES</th>"
                    info=info+"</tr>"
                    info=info+"<tr class='table-Light'>"                    
                    info=info+"<td>"+listapost[i]['nombre_actividad'] + "</td>" 
                    info=info+"<td>"+listapost[i]['nota'] + "</td>"
                    info=info+"<td>"+listapost[i]['retroalimentacion'] + "</td>"                   
                    info=info+"</tr>"
                    info=info+"</table>"
                
                }
                
             
                document.getElementById("listado1").innerHTML=info
                }
                )
                
                }

                function verestudiantesmatri(){
                    var listapost;
                    identificador =document.getElementById("id_session").innerHTML;
            
                    console.log(identificador)
                    var url="/estcal";
                    var data = {
                                "id_usuario": identificador                        
                        };
            
                    fetch(url, {
                    method: "POST",
                    body: JSON.stringify(data),
                    headers: {"Content-type":"application/json;charset=UTF-8"}
                        })
                    .then(response=>response.json())
                    .then((data)=>{
                    listapost=data;    
                    var info=""
                    
                    for(var i=0;i<listapost.length;i++)
                    {
                        info=info+"<tr class='table-warning'>"
                        info=info+"<td>"+listapost[i]['nombre'] + "</td>" 
                        info=info+"<td>"+listapost[i]['apellido'] + "</td>"
                        info=info+"<td>"+listapost[i]['nombre_materia'] + "</td>"                               
                        
                        info=info+"</tr>"
                    
                    }
                    
                 
                    document.getElementById("listado").innerHTML=info
                    }
                    )
                    
                    }

function accion(){
    let boton = document.getElementById('boton-accion');
    
    documento = document.getElementById('documento').value;
    nombre = document.getElementById('nombre').value;
    apellido = document.getElementById('apellido').value;
    rol = document.getElementById('rol').value;
    let persona = new profesor(documento,nombre,apellido,rol);

    if(boton.innerHTML=='Agregar'){
        Agregar(persona);
    }else{
        editar(persona);
    }
}

function Agregar(persona){

    if(persona.documento.trim() == ''){
        mostrarToast('documento no valido','#c0392b');
        return;
    }
    if(existe(persona.documento.trim())){
        mostrarToast('esta persona ya esta registrada','#c0392b');
        return;
    }

    personas.push(persona);
    mostrarToast('Agregado correctamente','#16a085');
    cargar_datos();
    limpiar();
}

function editar(persona){
    for (let i = 0; i < personas.length; i++) {
        if(personas[i].documento==persona.documento){
            mostrarToast('Modificado correctamente','#2980b9');
            personas[i] = persona;
            cargar_datos();
            limpiar();
            return;
        }
    }    
}

function limpiar(){
    document.getElementById('documento').value = '';
    document.getElementById('nombre').value = '';
    document.getElementById('apellido').value = '';
    document.getElementById('rol').value = 'seleccione';
    document.getElementById('documento').disabled = false;
    document.getElementById('boton-accion').innerHTML = 'Agregar';
}

function cargar(documento){
    for (let i = 0; i < personas.length; i++) {
        if(personas[i].documento==documento){
            document.getElementById('boton-accion').innerHTML = 'Editar';
            document.getElementById('documento').disabled = true;
            document.getElementById('documento').value= personas[i].documento;
            document.getElementById('nombre').value= personas[i].nombre;
            document.getElementById('apellido').value= personas[i].apellido;
            document.getElementById('rol').value = personas[i].rol;
            return;
        }
    }
}

function existe(documento){
    for (let i = 0; i < personas.length; i++) {
        if(personas[i].documento==documento){
            return true;
        }
    }
    return false;
}

function eliminar(documento){
    for (let i = 0; i < personas.length; i++) {
        if(personas[i].documento==documento){
            mostrarToast('Eliminado correctamente','#c0392b');
            personas.splice(i, 1);
            cargar_datos();
            return;
        }
    }
}


function mostrarToast(mensaje, color){
    let notificacion = document.getElementById('liveToast');
    let txtmensaje = document.getElementById('text-toast');
    txtmensaje.innerHTML = mensaje;
    notificacion.style.background = color;
    var toast = new bootstrap.Toast(notificacion);
    toast.show()
}