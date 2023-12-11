document.addEventListener("DOMContentLoaded", function() {
    const video = document.getElementById("video");
    const botonVideo1 = document.getElementById("cambiarVideo1");
    const botonVideo2 = document.getElementById("cambiarVideo2");
    const botonVideo3 = document.getElementById("cambiarVideo3");

    botonVideo1.addEventListener("click", function() {
        video.src = video1Url;
        video.load();
    });

    botonVideo2.addEventListener("click", function() {
        video.src = video2Url;
        video.load();
    });

    botonVideo3.addEventListener("click", function() {
        video.src = video3Url;
        video.load();
    });
});