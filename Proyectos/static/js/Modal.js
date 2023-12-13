// modal.js

function mostrarModal() {
    var modalBackground = document.getElementById('modalBackground');
    var modalContent = document.getElementById('modalContent');
  
    // Muestra el fondo y el contenido de la modal
    modalBackground.style.display = 'block';
    modalContent.style.display = 'block';
  }
  
  function ocultarModal() {
    var modalBackground = document.getElementById('modalBackground');
    var modalContent = document.getElementById('modalContent');
  
    // Oculta el fondo y el contenido de la modal
    modalBackground.style.display = 'none';
    modalContent.style.display = 'none';
  }
  