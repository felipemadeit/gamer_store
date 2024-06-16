document.addEventListener('DOMContentLoaded', function() {
    const decrementBtn = document.getElementById('decrement');
    const incrementBtn = document.getElementById('increment');
    const quantityInput = document.getElementById('quantity');

    decrementBtn.addEventListener('click', function() {
        //console.log("Down");
        decreaseQuantity();
    });

    incrementBtn.addEventListener('click', function() {
        //console.log("Up   "");
        increaseQuantity();
    });

    function decreaseQuantity() {
        let currentValue = parseInt(quantityInput.value, 10);
        if (currentValue > 1) {
            quantityInput.value = currentValue -1 ;
        }
    }

    function increaseQuantity() {
        let currentValue = parseInt(quantityInput.value, 10);
        if (currentValue < 15) {
            quantityInput.value = currentValue +1 ;
        }
    }
});
