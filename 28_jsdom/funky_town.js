//factorial function
var fact = function(n) {
  if (n > 1){
    return n * fact(n-1);
  }
    return 1;
}

//fibonocci function
var fib = function(n) {
  if (n == 0) {
    return 0;
  }
  if (n > 2) {
    return fib(n-1) + fib(n-2);
  }
  return 1;
}

// gcd(a,b) returns the greatest common divisor of the input numbers a and b
var gcd = function(a,b) {
  if (a == 0) {
    return b;
  }
  return gcd(b % a, a)
}

// array of students in SoftDev period 2
var studentsInPeriod2 = ["abedinM", "avrahamiB", "bhuiyanS", "caoW", "chanM", "chenE", "chenJ", "friedH",
"huangP", "huangT", "linD", "linW", "lupeaD", "mosesB", "niA", "olinJ", "olteanuA",
"rahmanM", "sontagC", "thompsonA", "wangD", "wuJ", "yusufovJ", "zenH"];

// randomStudent() returns a random student from the array studentsInPeriod2
var randomStudent = function() {
  randomNumber = Math.floor(Math.random() * studentsInPeriod2.length)
  return studentsInPeriod2[randomNumber]
}
//-----------------------------------------------------------------------------
//PRINTING fact(5)
var test = document.getElementById("a");
function firstCons() {
  console.log(fact(5));
}
function firstPage() {
  document.write(fact(5));
}
test.addEventListener("click", firstCons);
test.addEventListener("click", firstPage);

//PRINTING fib(5)
var test = document.getElementById("b");
function firstCons() {
  console.log(fib(5));
}
function firstPage() {
  document.write(fib(5));
}
test.addEventListener("click", firstCons);
test.addEventListener("click", firstPage);

//PRINTING gcd(10,15)
var test = document.getElementById("c");
function firstCons() {
  console.log(gcd(10,15));
}
function firstPage() {
  document.write(gcd(10,15));
}
test.addEventListener("click", firstCons);
test.addEventListener("click", firstPage);

//PRINTING randomStudent()
var test = document.getElementById("d");
var ans = randomStudent();
function firstCons() {
  console.log(ans);
}
function firstPage() {
  document.write(ans);
}
test.addEventListener("click", firstCons);
test.addEventListener("click", firstPage);
