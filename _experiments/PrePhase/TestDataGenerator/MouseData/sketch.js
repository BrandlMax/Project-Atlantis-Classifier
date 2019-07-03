console.log('Hello World');

let movementData = [];
let labelData = [];

function setup() {
  createCanvas(500, 500);
}

function draw() {
  background(0);
  movementData.push([mouseX, mouseY]);

  if (keyIsDown(49)) {
    console.log(1);
    labelData.push(1);
  } else if (keyIsDown(50)) {
    console.log(2);
    labelData.push(2);
  } else {
    labelData.push(3);
  }

  color(255);
  ellipse(mouseX, mouseY, 10, 10);
  drawGraph(movementData);
}

function drawGraph(movementData) {}

function mousePressed() {
  console.log('TEST');
  saveStrings(movementData, 'data_X.txt');
  saveStrings(labelData, 'labels_Y.txt');
  console.log('movementData', movementData.length);
  console.log('labelData', labelData.length);
}
