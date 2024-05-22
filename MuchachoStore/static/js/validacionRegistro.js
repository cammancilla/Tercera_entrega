// Cargar DOM

document.addEventListener("DOMContentLoaded", function () {

    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const rut = document.getElementById('rut');
    const correo = document.getElementById('correo');
    const edad = document.getElementById('edad');
    const password = document.getElementById('contraseña');
    const passwordConfirmacion = document.getElementById('confirmarContraseña');
    const button = document.getElementById("btnRegistro");
    const mensaje = document.getElementById("warnings");

    button.addEventListener("click", (e) => {
        e.preventDefault();



        // Regex Correo
        const regexCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        // Regex Password (8 caracteres, 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial)
        const regexPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$/;



        if (nombre.value == "" || nombre.value.length < 2) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Nombre no puede estar vacio o posee menos de 3 Caracteres</div>";
            mensaje.classList.add("alert-danger");
            console.log("Nombre no puede estar vacio");

            return;
        } else if (apellido.value == "" || apellido.value.length < 2) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Apellido no puede estar vacio o posee menos de 3 Caracteres</div>";
            mensaje.classList.add("alert-danger");
            console.log("Apellido no puede estar vacio");

            return;
        } else if (!regexCorreo.test(correo.value)) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Correo no valido</div>";
            mensaje.classList.add("alert-danger");
            console.log("Correo no valido");

            return;
        } else if (edad.value == "" || edad.value < 18) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Edad no puede estar vacio o ser menor a 18 años</div>";
            mensaje.classList.add("alert-danger");
            console.log("Edad no puede estar vacio");

            return;
        } else if (!regexPassword.test(password.value)) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Contraseña debe tener al menos 8 carácteres, una minuscula, 1 mayuscula, 1 numero y 1 caracter especial</div>";
            mensaje.classList.add("alert-danger");
            console.log("Contraseña no valida");

            return;
        } else if (password.value != passwordConfirmacion.value) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Contraseñas no coinciden</div>";
            mensaje.classList.add("alert-danger");
            console.log("Contraseñas no coinciden");

            return;
        } else {
            mensaje.innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>Datos validados correctamente</div>";
            mensaje.classList.add("alert-success");
            console.log("Datos validados correctamente");
        }

    });







});