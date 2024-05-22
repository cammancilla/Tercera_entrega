document.addEventListener("DOMContentLoaded", function () {
    const correo = document.getElementById('correo');
    const password = document.getElementById('passwordLogin');
    const button = document.getElementById("btnLogin");
    const mensaje = document.getElementById("warnings");

    button.addEventListener("click", (e) => {
        e.preventDefault();
        let entrar = false;
        // Regex Correo
        const regexCorreo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        // Regex Password (8 caracteres, 1 mayuscula, 1 minuscula, 1 numero, 1 caracter especial)
        const regexPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$/;
        if (!regexCorreo.test(correo.value)) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Correo no valido</div>";
            mensaje.classList.add("alert-danger");
            console.log("Correo no valido");
            entrar = true;
            return;
        }

        if (!regexPassword.test(password.value)) {
            mensaje.innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Contraseña debe tener al menos 8 carácteres, una minuscula, 1 mayuscula, 1 numero y 1 caracter especial</div>";
            mensaje.classList.add("alert-danger");
            console.log("Contraseña no valida");
            entrar = true;
            return;
        }

        if (!entrar) {
            mensaje.innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>Datos validados correctamente</div>";
            mensaje.classList.add("alert-success");
            console.log("Datos validados correctamente");
        }

    });
});
