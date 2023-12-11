$(document).ready(function() {
    // Configuración del token CSRF
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    var $calcularButton = $('#calcular');
    var $limpiarButton = $('#limpiar');
    var $resultado = $('#resultado');
    var $puntuacionActual = $('#puntuacion-actual');

    $calcularButton.click(function() {
        var total = 0;
        var moneda100 = parseInt($('#moneda-100').val()) || 0;
        var moneda200 = parseInt($('#moneda-200').val()) || 0;
        var moneda500 = parseInt($('#moneda-500').val()) || 0;
        var billete1000 = parseInt($('#billete-1000').val()) || 0;
        var billete2000 = parseInt($('#billete-2000').val()) || 0;
        var billete5000 = parseInt($('#billete-5000').val()) || 0;
        var billete10000 = parseInt($('#billete-10000').val()) || 0;
        var billete20000 = parseInt($('#billete-20000').val()) || 0;
        var billete50000 = parseInt($('#billete-50000').val()) || 0;
        var billete100000 = parseInt($('#billete-100000').val()) || 0;

        total = (moneda100 * 100) + (moneda200 * 200) + (moneda500 * 500) +
                (billete1000 * 1000) + (billete2000 * 2000) + (billete5000 * 5000) +
                (billete10000 * 10000) + (billete20000 * 20000) + (billete50000 * 50000) +
                (billete100000 * 100000);

        // Mostrar mensaje si el total es igual a cero
        if (total === 0) {
            $resultado.html('Aún no has empezado a ahorrar. ¡Anímate!');
            return;
        }

        // Mostrar mensaje dependiendo del total
        var mensaje = '';
        if (total < 5000) {
            mensaje = '¡Genial! Estás ahorrando poco, sigue así.';
        } else if (total < 20000) {
            mensaje = '¡Buen trabajo! Tu ahorro está mejorando.';
        } else {
            mensaje = '¡Increíble! Estás haciendo un gran trabajo con tus ahorros.';
        }

        // Mostrar el total y el mensaje
        $resultado.html('Encontraste un total de: $' + total + ' pesos colombianos. ' + mensaje);

        $.ajax({
            url: 'actividad01/actualizar_puntuacion/',
            type: 'POST',
            dataType: 'json',
            success: function(data) {
                $('#puntuacion-actual').text('Puntuación Actual: ' + data.puntuacion);
                alert(data.mensaje);
            },
            error: function(error) {
                console.error('Error al obtener la puntuación: ', error);
            }
        });
    });

    $limpiarButton.click(function() {
        $('input[type="number"]').val('');
        $resultado.html('');
    });
});


$(document).ready(function() {
    var $calcularButton = $('#calcular');
    var $limpiarButton = $('#limpiar');
    var $resultado = $('#resultado');
    var $puntuacionActual = $('#puntuacion-actual');

    $calcularButton.click(function() {
        var total = 0;
        var moneda100 = parseInt($('#moneda-100').val()) || 0;
        var moneda200 = parseInt($('#moneda-200').val()) || 0;
        var moneda500 = parseInt($('#moneda-500').val()) || 0;
        var billete1000 = parseInt($('#billete-1000').val()) || 0;
        var billete2000 = parseInt($('#billete-2000').val()) || 0;
        var billete5000 = parseInt($('#billete-5000').val()) || 0;
        var billete10000 = parseInt($('#billete-10000').val()) || 0;
        var billete20000 = parseInt($('#billete-20000').val()) || 0;
        var billete50000 = parseInt($('#billete-50000').val()) || 0;
        var billete100000 = parseInt($('#billete-100000').val()) || 0;

        total = (moneda100 * 100) + (moneda200 * 200) + (moneda500 * 500) +
                (billete1000 * 1000) + (billete2000 * 2000) + (billete5000 * 5000) +
                (billete10000 * 10000) + (billete20000 * 20000) + (billete50000 * 50000) +
                (billete100000 * 100000);

        // Mostrar mensaje si el total es igual a cero
        if (total === 0) {
            $resultado.html('Aún no has empezado a ahorrar. ¡Anímate!');
            return;
        }

        $.ajax({
            url: 'actualizar_puntuacion/',
            type: 'POST',
            data: { total: total },
            dataType: 'json',
            success: function(data) {
                $puntuacionActual.text('Puntuación Actual: ' + data.puntuacion);
                // Puedes eliminar esta línea si no quieres mostrar el mensaje de alerta
            },
            error: function(error) {
                console.error('Error al obtener la puntuación: ', error);
            }
        });
    });

    $limpiarButton.click(function() {
        $('input[type="number"]').val('');
        $resultado.html('');
    });
});
