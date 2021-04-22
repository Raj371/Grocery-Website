let addbtn = document.getElementsByClassName('responsive3');
// console.log(addbtn);
for (i = 0; i < addbtn.length; i++) {
    addbtn[i].addEventListener("click",upfunc)
};
function upfunc(e){
    alert("item has been added to the cart");
        let addToCartBtn = e.target;
        productContainer = addToCartBtn.parentElement.parentElement;
        productTitle = productContainer.getElementsByClassName('responsive1')[0].innerText;
        productPrice = productContainer.getElementsByClassName('productPrice')[0].innerText;
        let productQuan = productContainer.getElementsByClassName('responsive')[0];
        let productimgElm = productContainer.parentElement;
        productimg = productimgElm.getElementsByClassName('responsive7')[0].src;
        let notes = localStorage.getItem("notes");
        if(notes == null){
            notesObj = []
    }
     else{
        notesObj = JSON.parse(notes);
    }
    let myObj = {
title: productTitle,
price: productPrice,
imgsrc: productimg,
quan: productQuan.value
    }
    console.log(myObj.title);
    notesObj.push(myObj);
    
    localStorage.setItem("notes",JSON.stringify(notesObj));
    productQuan.value="";
       
};

