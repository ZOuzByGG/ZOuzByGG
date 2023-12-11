document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#verificarRespuestas").addEventListener("click", function () {
        // Verificar si todas las respuestas están seleccionadas
        if (
            document.querySelector("input[name='pregunta1']:checked") &&
            document.querySelector("input[name='pregunta2']:checked") &&
            document.querySelector("input[name='pregunta3']:checked") &&
            document.querySelector("input[name='pregunta4']:checked")
        ) {
            const respuestas = {
                pregunta1: document.querySelector("input[name='pregunta1']:checked").value,
                pregunta2: document.querySelector("input[name='pregunta2']:checked").value,
                pregunta3: document.querySelector("input[name='pregunta3']:checked").value,
                pregunta4: document.querySelector("input[name='pregunta4']:checked").value,
            };

            let respuestasCorrectas = 0;
            let retroalimentacion = "";

            // Verifica las respuestas y cuenta las correctas
            if (respuestas.pregunta1 === "Medio de intercambio") {
                respuestasCorrectas++;
            } else {
                retroalimentacion += "¡Respuesta incorrecta para la Pregunta 1! El dinero es un medio de intercambio que te permite comprar cosas y ahorrar para el futuro.<br>";
            }

            if (respuestas.pregunta2 === "Para comprar cosas") {
                respuestasCorrectas++;
            } else {
                retroalimentacion += "¡Respuesta incorrecta para la Pregunta 2! Ahorrar dinero es importante para comprar cosas que necesitas y para asegurar tu futuro.<br>";
            }

            if (respuestas.pregunta3 === "Trabajar") {
                respuestasCorrectas++;
            } else {
                retroalimentacion += "¡Respuesta incorrecta para la Pregunta 3! Una forma de ganar dinero es trabajando y esforzándote.<br>";
            }

            if (respuestas.pregunta4 === "En una cuenta de ahorros") {
                respuestasCorrectas++;
            } else {
                retroalimentacion += "¡Respuesta incorrecta para la Pregunta 4! Para guardar dinero de forma segura, es mejor utilizar una cuenta de ahorros en un banco.<br>";
            }

            // Muestra el puntaje
            document.querySelector("#resultado").innerHTML = `Tuviste ${respuestasCorrectas} respuestas correctas de 4 preguntas.`;

            // Muestra la retroalimentación
            document.querySelector("#feedback").innerHTML = retroalimentacion;
        } else {
            // Muestra un mensaje si no se han respondido todas las preguntas
            document.querySelector("#resultado").innerHTML = "Por favor, responde todas las preguntas antes de verificar.";
            document.querySelector("#feedback").innerHTML = "";
        }
    });
});
