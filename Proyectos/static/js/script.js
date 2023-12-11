document.addEventListener('DOMContentLoaded', function () {
    const checkButton = document.getElementById('checkButton');
    const result = document.getElementById('result');

    checkButton.addEventListener('click', function () {
        const price1 = parseFloat(document.getElementById('price1').value);
        const price2 = parseFloat(document.getElementById('price2').value);

        if (!isNaN(price1) && !isNaN(price2)) {
            if (price1 < price2) {
                result.textContent = '¡Correcto! El producto 1 es más barato.';
            } else if (price1 > price2) {
                result.textContent = '¡Correcto! El producto 2 es más barato.';
            } else {
                result.textContent = 'Ambos productos tienen el mismo precio.';
            }
        } else {
            result.textContent = 'Por favor, ingresa precios válidos.';
        }
    });
});
$(document).ready(function() {
    // Selector de fecha usando jQuery UI Datepicker
    $("#fecha-meta").datepicker();
});
