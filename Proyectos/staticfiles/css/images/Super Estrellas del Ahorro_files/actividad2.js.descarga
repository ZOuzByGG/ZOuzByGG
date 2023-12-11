// Variables para mantener el carrito y el total
const carrito = [];
let total = 0;

// Función para agregar productos al carrito
function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    total += precio;

    // Actualizar la vista del carrito y el total
    actualizarCarrito();
}

// Función para actualizar la vista del carrito y el total
function actualizarCarrito() {
    const carritoProductos = document.getElementById('carrito-productos');
    const totalElement = document.getElementById('total');

    // Limpiar el contenido previo del carrito
    carritoProductos.innerHTML = '';

    // Mostrar los productos en el carrito
    carrito.forEach((producto) => {
        const productoElement = document.createElement('p');
        productoElement.textContent = `${producto.nombre} - $${producto.precio} COP`;
        carritoProductos.appendChild(productoElement);
    });

    // Mostrar el total
    totalElement.textContent = `Total: $${total} COP`;
}

// Función para vaciar el carrito
function vaciarCarrito() {
    carrito.length = 0;
    total = 0;

    // Actualizar la vista del carrito y el total
    actualizarCarrito();
}

