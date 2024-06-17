document.addEventListener("DOMContentLoaded", function() {
// Selectores para el carrusel de procesadores
const prevButtonProcessors = document.querySelector(".show_products.processors .arrow-prev");
const nextButtonProcessors = document.querySelector(".show_products.processors .arrow-next");
const cardsContainerProcessors = document.querySelector(".show_products.processors .cards-container");
// Eventos para botones de navegación de procesadores
prevButtonProcessors.addEventListener("click", function() {
    cardsContainerProcessors.scrollBy({
        left: -247,
        behavior: "smooth"
    });
});
nextButtonProcessors.addEventListener("click", function() {
    cardsContainerProcessors.scrollBy({
        left: 247,
        behavior: "smooth"
    });
});
// Selectores para el carrusel de gráficos
const prevButtonGraphics = document.querySelector(".show_products.graphics .arrow-prev");
const nextButtonGraphics = document.querySelector(".show_products.graphics .arrow-next");
const cardsContainerGraphics = document.querySelector(".show_products.graphics .cards-container");
// Eventos para botones de navegación de gráficos
prevButtonGraphics.addEventListener("click", function() {
    cardsContainerGraphics.scrollBy({
        left: -247,
        behavior: "smooth"
    });
});
nextButtonGraphics.addEventListener("click", function() {
    cardsContainerGraphics.scrollBy({
        left: 247,
        behavior: "smooth"
    });
});
});


// Selectores para el carrusel de laptops
const prevButtonLaptops = document.querySelector(".show_products.laptops .arrow-prev");
const nextButtonLaptops = document.querySelector(".show_products.laptops .arrow-next");
const cardsContainerLaptops = document.querySelector(".show_products.laptops .cards-container");

// Eventos para botones de navegación de gráficos
prevButtonLaptops.addEventListener("click", function() {
    cardsContainerLaptops.scrollBy({
        left: -247,
        behavior: "smooth"
    });
});

nextButtonLaptops.addEventListener("click", function() {
    cardsContainerLaptops.scrollBy({
        left: 247,
        behavior: "smooth"
    });
});

// Selectores para el carrusel de laptops
const prevButtonKeyboards = document.querySelector(".show_products.keyboards .arrow-prev");
const nextButtonKeyboards = document.querySelector(".show_products.keyboards .arrow-next");
const cardsContainerKeyboards = document.querySelector(".show_products.keyboards .cards-container");

// Eventos para botones de navegación de gráficos
prevButtonKeyboards.addEventListener("click", function() {
    cardsContainerKeyboards.scrollBy({
        left: -247,
        behavior: "smooth"
    });
});

nextButtonKeyboards.addEventListener("click", function() {
    cardsContainerKeyboards.scrollBy({
        left: 247,
        behavior: "smooth"
    });
});





