//changes heading of html file
var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e.innerHTML;
};

//removes an item from regular list
var removeItem = function(e) {
};

//dynamic list items
var lis = document.getElementsByTagName("li");

// for (var i=0; i<lis.length; i++) {
//   console.log(lis[i].textContent);
//   lis[i].addEventListener('click', changeHeading(lis[i]));
//   lis[i].addEventListener('mouseout',  changeHeading(lis[i]));
//   lis[i].addEventListener('click', changeHeading(lis[i]));
// };



//add an item to regular list
var currentNum = 7;
var getNextItem = function() {
  currentNum += 1;
  currentItem = "item " + currentNum;
  console.log(currentItem);
};

var addItem = function(e) {
  var list = document.getElementById("thelist")
  var item = document.createElement("li")
  getNextItem();
  console.log(currentItem);
  item.appendChild(document.createTextNode(currentItem));
  list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

//add an item to fib list
var currentTerm = 0

var fib = function(n) {
  if (n < 2) {
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
};

var addFib = function(e) {
  console.log(currentTerm);
  var list = document.getElementById("fiblist")
  var item = document.createElement("li")
  item.appendChild(document.createTextNode(fib(currentTerm)));
  list.appendChild(item);
  currentTerm += 1;
};

// var addFib2 = function(e) {
//   console.log(e);
//   ???
//   ...
//   ???
// }

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
