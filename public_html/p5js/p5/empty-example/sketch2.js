var x, y; //współżędme obiektu
var krok = -1;
function setup() {
  // put setup code here
  createCanvas(600, 600);
  x = 575;
  y = 575;
}

function draw() {
  background(200);
  // put drawing code here
  //r = random(255);
  //g = random(255);
  //b = random(255);
  fill('yellow');
  strokeWeight(1);
  stroke('black');
  if (x > 14){
    x = x + krok;
  } else {
      x = - krok;
    }
  if (y > 14){
    y = y + krok;}
    else {
      y = y - krok;
    }
  ellipse(x, y, 30, 30);


}
