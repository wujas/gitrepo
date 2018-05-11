/*jshint esversion: 6*/

const canvasElem = document.getElementById('canvas');
const ctx = canvasElem.getContext('2d');

var szer = canvasElem.width, wys = canvasElem.height;
//kolor wypełnienia
ctx.fillStyle = "#8f14b8";
//rysujemy prostokąt/kwadraty
// x, y, width, height
ctx.fillRect(25, 25, 100, 100);

//kolor obrysu
ctx.fillStroke = "#cbcb18";
//drugi obrys prostokąta
ctx.strokeRect(30, 30, 100, 100);

//czyszczenia obrazu
ctx.clearRect(45, 45, 60, 60);

//rysowanie linii
// console.log(canvasElem.width / 2, canvasElem.height / 2);
ctx.moveTo(0, 0);
ctx.lineTo(canvasElem.width, canvasElem.height);
ctx.stroke();
ctx.moveTo(0, canvasElem.height);
ctx.lineTo( canvasElem.width, 0);
ctx.stroke();


//rysowanie kołaf
ctx.beginPath();
// x, y, radius, start, tre/false
ctx.arc(szer / 2, wys / 2, 100, 0, 2 * Math.PI);
ctx.arc(szer / 2, wys / 2, 90, 0,  Math.PI);

ctx.stroke();

ctx.beginPath();
ctx.arc(200, 100, 70, 0, 2 * Math.PI);
ctx.stroke();

// tekst
ctx.lineWidth = 1;
ctx.font = "normal 40px Arial";
ctx.textBaseline = "middle";
ctx.textAlign = "left";
ctx.strokeText('$$$$$$$$', 70, 180);
