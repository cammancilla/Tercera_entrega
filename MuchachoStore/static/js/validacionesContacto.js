document.addEventListener("DOMContentLoaded", function () {
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const correo = document.getElementById('correo');
    const telefono = document.getElementById('telefono');
    const comentario = document.getElementById('comentario');
    const boton = document.getElementById('btnContacto');
    const mensaje = document.getElementById('warnings');

    if (boton) {
        boton.addEventListener("click", (e) => {
            e.preventDefault();

            // Limpiar mensajes anteriores
            mensaje.innerHTML = '';
            mensaje.className = '';

            // Regex correo
            const regexCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

            if (!nombre.value || nombre.value.length < 3) {
                mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Nombre no puede estar vacío o tener menos de 3 caracteres</div>";
                mensaje.classList.add("alert-danger");
                console.log("Nombre no válido");
                return;
            }

            if (!apellido.value || apellido.value.length < 3) {
                mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Apellido no puede estar vacío o tener menos de 3 caracteres</div>";
                mensaje.classList.add("alert-danger");
                console.log("Apellido no válido");
                return;
            }

            if (!regexCorreo.test(correo.value)) {
                mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Correo no válido</div>";
                mensaje.classList.add("alert-danger");
                console.log("Correo no válido");
                return;
            }

            if (!telefono.value || telefono.value.length < 8) {
                mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Teléfono debe tener al menos 8 dígitos</div>";
                mensaje.classList.add("alert-danger");
                console.log("Teléfono no válido");
                return;
            }

            if (!comentario.value || comentario.value.length < 10) {
                mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>El comentario debe tener al menos 10 caracteres</div>";
                mensaje.classList.add("alert-danger");
                console.log("Comentario muy corto");
                return;
            }

            // Si todo está correcto, enviar el formulario
            mensaje.innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>Datos validados correctamente. Enviando...</div>";
            mensaje.classList.add("alert-success");
            
            // Enviar formulario después de un breve delay para mostrar el mensaje
            setTimeout(() => {
                document.getElementById('formularioContacto').submit();
            }, 1000);
        });
    }
});