document.addEventListener("beforeunload" , ()=>{
    
    } )  
    function pr(){
        let o = document.cookie.split(';')
        let p ;
        for(let i = 0 ; i < o.length;i++){
           p = o[i].split('=')
        }
        let o1 = p[1]
        // console.log(p)
        // o1 = o1[1]   
        let item203 = document.querySelectorAll(".shop-item").forEach(el=>{
            
            if(el.dataset.content == o1){
                el.classList.add("active")
            }

        })
    
        let content203 = document.querySelectorAll('.shop_content').forEach(le=>{
            if(le.dataset.content == o1){
                le.classList.add("active")
            }
        })
    } 
    pr()
function headerSlader(n){
    let headerSladerActive = document.querySelector('.header-slader-item[data-active]')
    let headerSladerHasDots = document.querySelectorAll('.header-slader-item[data-hasdot]')
    let headerSladerItems = [...document.querySelectorAll('.header-slader-item')]
    let headerSladerCurrentIndex = headerSladerItems.indexOf(headerSladerActive )
    let headerSladerCurrentItem = headerSladerCurrentIndex + n;

    if(headerSladerCurrentItem < 0 )headerSladerCurrentItem = headerSladerItems.length -1;
    if(headerSladerCurrentItem > (headerSladerItems.length -1))headerSladerCurrentItem = 0;

    headerSladerItems[headerSladerCurrentItem].dataset.active = true;
    delete headerSladerActive.dataset.active;
   
    dotHeaderSlader(headerSladerCurrentItem);
  

    
}

let piu = document.querySelectorAll(".dotHeaderSladera")[0];

if(piu) {
    piu.addEventListener('click',(event)=>{

    if(event.target.classList == "dotHeaderItem"){
        dotHeaderSlader(1);
        headerSlader(1)
        
     }
    })
 }

function dotHeaderSlader(n){
    let sladerHeaderDotList = [...document.querySelectorAll('.dotHeaderItem')];
    
    for(let t = 0; t < sladerHeaderDotList.length;t++){
        sladerHeaderDotList[t].classList.remove('active')
    }
    sladerHeaderDotList[n].classList.toggle('active');
}


const btnNextSladerHeader = ()=>headerSlader(1);
const btnPrevSladerHeader = ()=>headerSlader(-1);





















// let dotsList = ;
// let headerSladerHasDots = document.querySelectorAll('.header-slader-item[data-active][data-hasdot]')
// dotsList.addEventListener('click',(event)=>{

//     if(event.target.classList == "dotHeaderItem"){
//         dotHeaderSlader(elementProgress())
       
        
//     }
// })

function elementProgress(){
    return document.querySelector('.header-slader-item[data-active][data-hasdot]').dataset.hasdot
}
///----------------------------------------

// let offset = 1150;
// let offsetNext = 1200;
// let btnSladerNewPrevCollection = document.querySelector('.btnSladerNewPrevCollection');
// let btnSladerNewNextCollection = document.querySelector('.btnSladerNewNextCollection');
// let sladerCollectionConteinerLine =  document.querySelector('.sladerCollectionConteiner-list');
// btnSladerNewPrevCollection.addEventListener('click',()=>{
//     plusSladerNewCollections(400);
// })
// console.log(btnSladerNewNextCollection)
// btnSladerNewNextCollection.addEventListener('click',()=>{
//     minSladerNewCollections(400);
// })

// function plusSladerNewCollections(n){
//     offset+=n
//     if(offset > 1150){
//         offset = 0
//     }
   
//     sladerCollectionConteinerLine.style.right = offset + 'px' ;
  
// }

// function minSladerNewCollections(n){
//     offsetNext -= n
   
//     if(offsetNext < 0){
//         offsetNext = 1200
//     }
//     sladerCollectionConteinerLine.style.right = offsetNext + 'px' ;
  
// }


let offset = 0;

let btnSladerNewPrevCollection = document.querySelector('.sladerCollectionConteiner-item:first-of-type> div button');
let btnSladerNewNextCollection = document.querySelector('.sladerCollectionConteiner-item:last-of-type> div button');
let sladerCollectionConteinerLine =  document.querySelector('.sladerCollectionConteiner-list');
let sladerCollectionConteinerItem =  document.querySelector('.sladerCollectionConteiner-item');
let arraySladerItemCollecrions;
// console.log(sladerCollectionConteinerLine)""?|
if(sladerCollectionConteinerLine != undefined || sladerCollectionConteinerLine != null){
    arraySladerItemCollecrions = [...sladerCollectionConteinerLine.children];



btnSladerNewNextCollection.addEventListener('click',()=>{
    let firstElents = arraySladerItemCollecrions[0];
    arraySladerItemCollecrions.shift(arraySladerItemCollecrions[0])
    arraySladerItemCollecrions.push(firstElents)
    sladerCollectionConteinerLine.appendChild(...arraySladerItemCollecrions); 
    
})



btnSladerNewPrevCollection.addEventListener('click',()=>{
    let firstElents = arraySladerItemCollecrions[arraySladerItemCollecrions.length-1];
    arraySladerItemCollecrions.pop(arraySladerItemCollecrions[firstElents]);
    arraySladerItemCollecrions.unshift(firstElents)
    sladerCollectionConteinerLine.appendChild(...arraySladerItemCollecrions); 
    

})
}


let dotsComands = document.querySelectorAll('.dotComands')
function comandSlader(n,u = null){
    let activeItem = document.querySelector('.sladerComand-item[data-active]');
    let listItems = [...document.querySelectorAll('.sladerComand-item')];
    let indexCurrent = listItems.indexOf(activeItem);
    let itemCurrent = indexCurrent + n;
    
    
    if(itemCurrent < 0){
        itemCurrent = listItems.length-1;
    }
    if(itemCurrent > (listItems.length)-1){
        itemCurrent = 0;
    }
    if(u !== null && u !== listItems.length){
        listItems[u].dataset.active = true;
        delete activeItem.dataset.active;
       
    }else{
        listItems[itemCurrent].dataset.active = true;
        delete activeItem.dataset.active;
    }
    
    



     

   if(u == null){
    for(let i = 0; i < dotsComands.length; i++){
        
            if((dotsComands[i].dataset.dot) == (listItems[itemCurrent].dataset.hasdot) ){
                dotsComands[i].classList.add('active');
            
            }else{
            dotsComands[i].classList.remove('active');
            }

        }

   }
    


}


let btnComandsSladerNext = document.querySelector('.btnSladerComandsNext');
let btnComandsSladerPrev = document.querySelector('.btnSladerComandsPrev');

if( btnComandsSladerNext != undefined){
    btnComandsSladerNext.addEventListener('click',()=>{
    comandSlader(1);})
}

if(btnComandsSladerPrev != undefined){
    btnComandsSladerPrev.addEventListener('click',()=>{
        comandSlader(-1);
        
    })

}
    







let listItemsOut =[...document.querySelectorAll('.sladerComand-item')]
for(let i = 0 ; i < dotsComands.length;i++){
    dotsComands[i].addEventListener('click',(event)=>{
        // comandSlader(dotsComands[i].dataset.dot)
        if(event.target){
            for(let j = 0 ; j < dotsComands.length;j++){
                dotsComands[j].classList.remove('active')
             }
            dotsComands[i].classList.add('active');
        }

        let index = dotsComands[i].dataset.dot;
        
        comandSlader(1,--index)

    // for(let y = 0;y < listItemsOut.length;y++){
    //     delete listItemsOut[y].dataset.active;
    // }
    // listItemsOut[dotsComands[i].dataset.dot].dataset.active = true; 








    })
}

let obert = document.querySelector('.blockOberts');
let burder = document.querySelector('.btnBurder');
let contentBurger = document.querySelector('.burgerContent');
let headerList = document.querySelector('.header-list');
let contact = document.querySelector('.headerLogoContact');
let contactItem = contact.innerHTML;
let contactLi = document.createElement('a');

contactLi.classList.add('headerLogoContact');
contactLi.classList.add('headerLogoContactIsJs');
contactLi.innerText = contactItem;
// console.log(contactLi)
burder.addEventListener('click',()=>{
    contentBurger.innerHTML =  headerList.innerHTML;
    // contentBurger.appendChild(contactLi);
    console.log(contentBurger)
    if(contentBurger.style.display == "block"){
        contentBurger.style.display = "none";
        obert.style.display = 'none'
    }else{
        contentBurger.style.display = "block"
        obert.style.display = 'block'
    }
    
})
obert.addEventListener('click',()=>{
    if(contentBurger.style.display == "block"){
        contentBurger.style.display = "none";
        obert.style.display = 'none'
    }else{
        contentBurger.style.display = "block"
        obert.style.display = 'block'
    }
})

let spanRow = document.querySelectorAll(".basketContentitem-img>span");
let countBasketElements = document.querySelector(".countProduct");
let countsBasket =  document.querySelectorAll(".basketBody>tr");

let number = countsBasket.length;
// console.log(number)
// countBasketElements.innerHTML = number;

for(let i = 0 ; i < spanRow.length ; i++){
    spanRow[i].addEventListener('click',()=>{
        spanRow[i].parentElement.parentElement.parentElement.removeChild(spanRow[i].parentElement.parentElement);
        // countBasketElements.innerHTML = countsBasket.length+1;
        // number--;
        // countBasketElements.innerHTML = --number;
    })
}
//  = Number(number);
let formCount = document.querySelectorAll('.formaCount')



function fun(){

}
formCount.forEach(it=>{

    it.addEventListener('submit',(event)=>{
        event.preventDefault()
        fun()
    })

    it.addEventListener('blur',function (event){
        fun()
        it.submit()
        
    },true)
})

try{
    let item = document.querySelectorAll(".shop-item")
    let content = document.querySelectorAll('.shop_content')
    for(let i = 0; item.length;i++){
      
        item[i].addEventListener('click',(event)=>{
            for(let u = 0 ; u < item.length; u++){
                item[u].classList.remove('active')
                
            }
          
            if(event.target){
                event.target.classList.add('active')
                let current = event.target.dataset.content
                let content = document.querySelectorAll('.shop_content[data-content]')
                document.cookie = "name="+current
                console.log(sessionStorage.getItem('name'))
                for(let i = 0 ; i < content.length; i++){

                 
                       
                        content[i].classList.remove('active')
                    
                    if(content[i].dataset.content == current){     
                      content[i].classList.add('active')
                        }
                    
                }
            }
               
       
        })  
       
    }
    // )
}
catch{

}
try{
   document.getElementById('id_username').placeholder = 'Логин';
document.getElementById('id_password').placeholder = 'Пароль';
 document.getElementById('id_username').classList.add('ob_input')  
}
catch{

}
try{
    document.getElementById('id_email').placeholder = 'Email'; 
}
catch{

}
try{
     let ps = document.getElementById('id_password1'),
    ps2 = document.getElementById('id_password2'),
    form = document.getElementById('reg_form')
    form_sub = document.getElementById('reg_form_sub')
    form_sub.addEventListener('click',(event)=>{
        event.preventDefault()
        console.log(ps.value)
        if(ps.value == ps2.value && ps.value != ''){
            form.submit()
        }
        else if(ps.value != ''){
            document.getElementById('ansver').innerHTML = "Пароли не совпадают"
        }
        
        
        
      
    })
}
   catch{
    
   }



