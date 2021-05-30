let notes = localStorage.getItem("notes");

if (notes == null) {
  notesObj = [];
} else {
  notesObj = JSON.parse(notes);
}

let html = "";
let a = 0;
notesObj.forEach(function (element, index) {
  a = a + element.price * element.quan;
  html =
    html +
    `<div class="container">
      <table>
          <thead>
              <tr>
              <th class="y1">Image</th>
              <th class="y2">Title</th>
              <th class="y3">Quantity</th>
              <th class="y4">Price</th>
              <th class="y5">Option</th>
          </tr>
          </thead>
          <tbody>
              <tr>
              <td class="y1"><img src="${element.imgsrc}"></td>
              <td class="y2">${element.title}</td>
              <td class="y3">${element.quan}</td>
              <td class="y4">${element.quan*element.price}Rs</td>
              <td><button class="deleteitembutton" id="${index}"  onclick="deleteNote(this.id)" >Delete</button></td>
          </tr>
          </tbody>
      </table>
  </div>`

;
});
a=`<div class="cartfruitmr">Total amount is ${a} Rs</div>`;
let flex = document.getElementById("flex");
let flexs = document.getElementById("flexs");
try{
if (notesObj.length != 0) {
  flex.innerHTML = html;
  flexs.innerHTML=a;
} else {
  flex.innerHTML = "Nothing to show! Please order something";
}
}
catch(e)
{
  console.log(e);
}
function order(){
  alert("You have successfully ordered and items would be delivered within 1- 2 days ");
  // window.location.href="/Grocery1";
  $.ajax({
      type:'POST',
      url:'/order',
      data:{},
      contentType:"application/json; charset=utf-8"
  });
  console.log("order items" );
  };

function deleteNote(index) {
  //   console.log("I am deleting", index);
  console.log(index)
  
  $.ajax({
    type:'POST',
    url:'/delete',
    data:JSON.stringify({'index':index}),
    contentType:"application/json; charset=utf-8",
    success:function(response){
      console.log("success");
    setTimeout(window.location.href='/Cart',500);
    }

  }
  );


  console.log("raj")

  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = [];
  } else {
    notesObj = JSON.parse(notes);
  }

  notesObj.splice(index, 1);
  console.log(notesObj);
  localStorage.setItem("notes", JSON.stringify(notesObj));
  localStorage.getItem("notes");

  let html = "";
  let a = 0;
  notesObj.forEach(function (element, index) {
    a = a + element.price * element.quan;
    html =
      html +
      `<div class="container">
      <table>
          <thead>
              <tr>
              <th class="y1">Image</th>
              <th class="y2">Title</th>
              <th class="y3">Quantity</th>
              <th class="y4">Price</th>
              <th class="y5">Option</th>
          </tr>
          </thead>
          <tbody>
              <tr>
              <td class="y1"><img src="${element.imgsrc}"></td>
              <td class="y2">${element.title}</td>
              <td class="y3">${element.quan}</td>
              <td class="y4">${element.quan*element.price}Rs</td>
              <td><button class="deleteitembutton" id="${index}"  onclick="deleteNote(this.id)" >Delete</button></td>
          </tr>
          </tbody>
      </table>
  </div>`

;
  });
  a=`<div class="cartfruitmr">Total amount is ${a} Rs</div>`;
  try{
  let flex = document.getElementById("flex");
  let flexs = document.getElementById("flexs");
  if (notesObj.length != 0) {
    flex.innerHTML = html;
    flexs.innerHTML=a;
  } else {
    flex.innerHTML ="Nothing to show! Use Add a Note section above to add notes.";
      flexs.innerHTML="Total amount is 0";
  }
  }
  catch(e){
    console.log(e);
  }
}


