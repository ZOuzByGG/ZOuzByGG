document.addEventListener("DOMContentLoaded", function () {
  const imagenAlex = document.getElementById("imagen-alex");
  const botonAhorrar = document.getElementById("ahorrar");
  const botonGastar = document.getElementById("gastar");
  const resultado = document.getElementById("resultado");
  const historia = document.getElementById("historia");

  botonAhorrar.addEventListener("click", function () {
      imagenAlex.src = staticBasePath + "js/alex-contento.png";
      resultado.textContent = "¡VAMOS! Alex tomó una decisión sabia y decidió ahorrar su dinero en lugar de gastarlo. Después de un tiempo, finalmente pudo comprar ese ukelele que tanto deseaba. ¡Ahora es un gran músico!";
      mostrarHistoriaAhorrar();
  });

  botonGastar.addEventListener("click", function () {
      imagenAlex.src = staticBasePath + "js/alex-triste.png";
      resultado.textContent = "¡Qué triste! Alex gastó todo su dinero en dulces y no pudo comprar el ukelele que siempre ha querido.";
      mostrarHistoriaGastar();
  });


});
