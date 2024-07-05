document.addEventListener('DOMContentLoaded', loadEventListeners);

let allContainerCart = document.querySelector('.products');
let containerBuyCart = document.querySelector('.card-cart');

let buyThings = [];

function loadEventListeners() {
    allContainerCart.addEventListener('click', addProduct);
    containerBuyCart.addEventListener('click', deleteProduct);
}

function addProduct(e) {
    if (e.target.classList.contains('btn-add-cart')) {
        const selectedProduct = e.target.closest('.product');
        readTheContent(selectedProduct);
    }
}

function readTheContent(product) {
    const infoProduct = {
        image: product.querySelector('img').getAttribute("src"),
        title: product.querySelector('.card-title').textContent,
        price: product.querySelector('.precio').textContent,
        id: product.querySelector('button').getAttribute('data-id'),
        amount: 1
    };

    const exists = buyThings.some(product => product.id === infoProduct.id);
    if (exists) {
        const products = buyThings.map(product => {
            if (product.id === infoProduct.id) {
                product.amount++;
                return product;
            } else {
                return product;
            }
        });
        buyThings = [...products];
    } else {
        buyThings = [...buyThings, infoProduct];
    }
    loadHtml();
}

function loadHtml() {
    clearHtml();
    buyThings.forEach(product => {
        const { image, title, price, amount, id } = product;
        const row = document.createElement('div');
        row.classList.add('card');
        row.innerHTML = `
            <img src="${image}" alt="Product image" width="400px" height="80px">
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="precio">${price}</p>
                <h6> Amount: ${amount}</h6>
                <span class="delete-product" data-id="${id}">X</span>
            </div>
        `;
        containerBuyCart.appendChild(row);
    });
}

function clearHtml() {
    containerBuyCart.innerHTML = '';
}

function deleteProduct(e) {
    if (e.target.classList.contains('delete-product')) {
        const productId = e.target.getAttribute('data-id');
        buyThings = buyThings.filter(product => product.id !== productId);
        loadHtml();
    }
}
