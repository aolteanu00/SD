//factorial function
var fact = function(n) {
  if (n > 1){
    return n * fact(n-1);
  }
  else {
    return 1;
  }
}

//fibonocci function
var fib = function(n) {
  if (n == 0) {
    return 0;
  }
  if (n > 2) {
    return fib(n-1) + fib(n-2);
  }
  else {
    return 1;
  }
}
