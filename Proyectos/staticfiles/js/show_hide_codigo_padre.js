// show_hide_codigo_padre.js

document.addEventListener('DOMContentLoaded', function () {
    var fechaNacimientoInput = document.getElementById('id_birthdate');
    var codigoPadreField = document.getElementById('codigoPadreField');

    fechaNacimientoInput.addEventListener('change', function () {
        var fechaNacimiento = new Date(fechaNacimientoInput.value);
        var hoy = new Date();
        var edad = hoy.getFullYear() - fechaNacimiento.getFullYear();

        // Verificar si el usuario es menor de 18 años
        if (edad < 18) {
            codigoPadreField.style.display = 'block';
        } else {
            codigoPadreField.style.display = 'none';
        }
    });
});
