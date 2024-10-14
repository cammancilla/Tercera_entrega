document.addEventListener("DOMContentLoaded", function () {
    console.log("El DOM se ha cargado correctamente"); // Para verificar si el evento se dispara

    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const correo = document.getElementById('correo');
    const telefono = document.getElementById('telefono');
    const comentario = document.getElementById('comentario');
    // * Botón de envío del formulario y mensaje de advertencia
    const boton = document.getElementById('btnContacto');
    const mensaje = document.getElementById('warnings');

    boton.addEventListener("click", (e) => {
        e.preventDefault();

        // Limpiar mensajes previos
        mensaje.innerHTML = '';

        let warnings = '';
        let enviar = true;

        // Regex correo
        const regexCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

        if (nombre.value === '' || nombre.value.length < 3) {
            warnings += "<div class='alert alert-danger'>Nombre no puede estar vacío o poseer menos de 3 caracteres</div>";
            enviar = false;
        }

        if (apellido.value === '' || apellido.value.length < 3) {
            warnings += "<div class='alert alert-danger'>Apellido no puede estar vacío o poseer menos de 3 caracteres</div>";
            enviar = false;
        }

        if (!regexCorreo.test(correo.value)) {
            warnings += "<div class='alert alert-danger'>Correo no es válido</div>";
            enviar = false;
        }

        if (telefono.value === '' || telefono.value.length < 8) {
            warnings += "<div class='alert alert-danger'>Teléfono no puede estar vacío o debe tener al menos 8 dígitos</div>";
            enviar = false;
        }

        if (comentario.value === '' || comentario.value.length < 10) {
            warnings += "<div class='alert alert-danger'>Comentario no puede estar vacío o debe tener al menos 10 caracteres</div>";
            enviar = false;
        }

        if (!enviar) {
            mensaje.innerHTML = warnings;
        } else {
            mensaje.innerHTML = "<div class='alert alert-success'>Formulario enviado correctamente</div>";
        }
    });
});
