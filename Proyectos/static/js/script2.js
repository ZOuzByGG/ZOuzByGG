document.addEventListener('DOMContentLoaded', function () {
    const calculateButton = document.getElementById('calculateButton');
    const total = document.getElementById('total');

    calculateButton.addEventListener('click', function () {
        const quantity1 = parseInt(document.getElementById('quantity1').value);
        const quantity2 = parseInt(document.getElementById('quantity2').value);
        const price1 = 10; // Precio del Producto 1
        const price2 = 15; // Precio del Producto 2

        if (!isNaN(quantity1) && !isNaN(quantity2)) {
            const totalPrice = quantity1 * price1 + quantity2 * price2;
            total.textContent = `Total a pagar: $${totalPrice}`;
        } else {
            total.textContent = 'Por favor, ingresa cantidades válidas.';
        }
    });
});
