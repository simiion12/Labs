float x, y; // Declare x and y as float variables
int rx, ry; // Declare rx and ry as integer variables

void setup() {
  size(400, 400);
  background(51);
  x = 200; // Center of the rectangle
  y = 200; // Center of the rectangle
  rx = 180; // Half of the rectangle's width
  ry = 150; // Half of the rectangle's height
  rectMode(RADIUS);
  rect(x, y, rx, ry);
  // Draw the diagonal line
  line(x - rx, y - ry, x + rx, y + ry);
  
  // Draw the diagonal line
  line(x - rx, y + ry, x + rx, y - ry);
  
  // Draw horizontal center line
  line(x - rx, y, x + rx, y);
  
  // Draw vertical center line
  line(x, y - ry, x, y + ry);
  
}

void draw() {
  strokeWeight(2);
  
  //Draw an arc in first quadrant
  stroke(0, 0, 255);
  arc(x, y, rx * 2, ry * 2, -PI/2, 0);
  
  //Draw an arc in  in middle of quadrant II the end of quadrant III
  stroke(255,0,0);
  arc(x, y, rx * 2, ry * 2, PI/2, PI + PI/4, CHORD);
  
  //Draw an arc in end of quadrant IV and the middle of quadrant III
  stroke(0,255,0);
  arc(x, y, (rx - 10) * 2, ry * 2, 0, PI + PI/4 , PIE);
}
