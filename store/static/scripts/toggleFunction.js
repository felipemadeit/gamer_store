function toggleItems() {
    const items = document.querySelectorAll('.order-by');

    items.forEach(item => {
        if(item.style.display === 'none') {
            item.style.display = 'inline-block';
        } else  {
            item.style.display = 'none'
        }
    });
}