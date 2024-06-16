document.addEventListener("DOMContentLoaded", function() {
    const prevButton = document.querySelector(".arrow-prev");
    const nextButton = document.querySelector(".arrow-next");
    const cardsContainer = document.querySelector(".cards-container");

    // Listener para la flecha izquierda (prev)
    prevButton.addEventListener("click", function() {
        cardsContainer.scrollBy({
            left: -300, // Ajusta la cantidad de desplazamiento según el ancho de tus tarjetas
            behavior: "smooth" // Desplazamiento suave
        });
    });

    // Listener para la flecha derecha (next)
    nextButton.addEventListener("click", function() {
        cardsContainer.scrollBy({
            left: 300, // Ajusta la cantidad de desplazamiento según el ancho de tus tarjetas
            behavior: "smooth" // Desplazamiento suave
        });
    });
});
