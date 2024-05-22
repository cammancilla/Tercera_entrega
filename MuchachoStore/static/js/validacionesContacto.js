document.addEventListener("DOMContentLoaded", function () {


    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const correo = document.getElementById('correo');
    const telefono = document.getElementById('telefono');
    const comentario = document.getElementById('comentario');

    const boton = document.getElementById('btnContacto');
    const mensaje = document.getElementById('warning');

    boton.addEventListener("click", (e) => {
        e.preventDefault();


        // Regex correo
        const regexCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

        if (nombre.value == '' || nombre.value.length < 2) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Nombre no puede estar vacio o posee menos de 3 Caracteres</div>";
            mensaje.classList.add("alert-danger");
            console.log("Nombre no puede estar vacio");
            return;

        }
    });










});