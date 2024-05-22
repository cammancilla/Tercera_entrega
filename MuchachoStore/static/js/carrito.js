let allContainerCart = document.querySelector('.products');
let containerBuyCart = document.querySelector('.card-cart')


let buyThings = [];

function loadEventListenrs(){
    allContainerCart.addEventListener('click', addProduct);
}

function addProduct(e){
    //e.preventDefault();
   
    if(e.target.classList.contains('btn-add-cart')){
    const selectProduct = e.target.parentElement.parentElement;
    readTheContent(selectProduct);
    console.log("Test");
    }
}

function readTheContent(product){
    const infoProduct = {
        image: product.querySelector('img').getAttribute("src"),
        title: product.querySelector('.card-title').textContent,
        price: product.querySelector('.precio').textContent,
        id: product.querySelector('button').getAttribute('data-id'),
        amount: 1
    } 
    buyThings = [...buyThings, infoProduct]
    loadHtml();
    console.log(infoProduct);
}

function loadHtml(){
    // clearHtml();
    buyThings.forEach(product => {
        const {image, title, price, amount, id} = product;
        const row = document.createElement('div');
        row.classList.add('card');
        row.innerHTML = `
        <img src="${image}" alt="cargando..." width="400px" heigth="80px">
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

//function clearHtml(){
    //containerBuyCart.innerHTML = '';
//}
