// Obtén la referencia a la hucha y a todas las monedas
const hucha = document.getElementById('hucha');
const monedas = document.querySelectorAll('.moneda');
const mensaje = document.getElementById('mensaje'); // Obtén el elemento del mensaje

// Agrega un controlador de eventos para el evento "dragstart" en las monedas
monedas.forEach((moneda) => {
  moneda.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', e.target.id); // Establece el ID de la moneda como dato arrastrado
  });
});

// Agrega un controlador de eventos para el evento "dragover" en la hucha
hucha.addEventListener('dragover', (e) => {
  e.preventDefault(); // Evita el comportamiento predeterminado (permitir soltar elementos)
});

// Agrega un controlador de eventos para el evento "drop" en la hucha
hucha.addEventListener('drop', (e) => {
  e.preventDefault(); // Evita el comportamiento predeterminado (permitir soltar elementos)
  
  // Obtiene el ID de la moneda que se soltó
  const monedaID = e.dataTransfer.getData('text/plain');
  
  // Busca la moneda por su ID y verifica si es válida
  const monedaArrastrada = document.getElementById(monedaID);
  if (monedaArrastrada) {
    // Oculta la moneda arrastrada (imagen)
    monedaArrastrada.style.display = 'none';
    
    // Verifica si todas las monedas se han ocultado
    let todasOcultas = true;
    monedas.forEach((moneda) => {
      if (moneda.style.display !== 'none') {
        todasOcultas = false;
        return;
      }
    });
  
    // Si todas las monedas están ocultas, muestra un mensaje
    if (todasOcultas) {
      mensaje.textContent = 'Has recolectado todas las monedas FELICIDADES. RECUERDA QUE CADA MONEDA HACE LA DIFERENCIA A LA HORA DE AHORRAR';
    }
  }
});
