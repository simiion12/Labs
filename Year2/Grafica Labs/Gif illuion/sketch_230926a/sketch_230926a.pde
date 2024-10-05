int numRaindrops = 300; // Number of raindrops
Raindrop[] raindrops = new Raindrop[numRaindrops]; // Array to store raindrops
float[] cloudX = {0, 100, 200}; // Clouds' initial positions
float[] cloudSpeed = {1, 1.5, 2}; // Clouds' horizontal speeds
int numClouds = cloudX.length; // Number of clouds
Bird[] birds = new Bird[8]; // Array to store birds
int numBirds = birds.length; // Number of birds

void setup() {
  size(400, 400);
  noStroke();//remove the outline

  // Create raindrops
  for (int i = 0; i < numRaindrops; i++) {
    raindrops[i] = new Raindrop();
  }

  // Create birds
  for (int i = 0; i < numBirds; i++) {
    birds[i] = new Bird(random(width), random(50, 150));
  }
}

void draw() {
  // Background
  background(135, 206, 235); // Light Blue Sky

  // Sun
  fill(255, 255, 0); // Yellow
  ellipse(350, 50, 80, 80); // Sun

  // Grass
  fill(0, 128, 0); // Green
  rect(0, 300, width, height - 300); // Grass

  // House
  fill(255, 0, 0); // Red
  rect(180, 200, 100, 100); // House Base
  fill(128, 0, 0); // Dark Red
  triangle(175, 200, 275, 200, 225, 150); // Roof

  // Windows
  fill(255); // White
  rect(200, 220, 30, 30); // Window 1
  rect(245, 220, 30, 30); // Window 2

  // Door
  fill(139, 69, 19); // Brown
  rect(220, 260, 40, 40); // Door

  // Trees
  drawTree(50, 250);
  drawTree(120, 280);
  drawTree(280, 280);
  drawTree(350, 250);

  // Draw clouds
  for (int i = 0; i < numClouds; i++) {
    drawCloud(cloudX[i], 80);
    cloudX[i] += cloudSpeed[i];

    if (cloudX[i] > width) {
      cloudX[i] = -200;
    }
  }

  // Draw raindrops
  for (int i = 0; i < numRaindrops; i++) {
    raindrops[i].fall();
    raindrops[i].display();
  }

  // Draw birds
  for (int i = 0; i < numBirds; i++) {
    birds[i].fly();
    birds[i].display();
  }
}

void drawTree(float x, float y) {
  // Tree Trunk
  fill(139, 69, 19); // Brown
  rect(x - 10, y, 20, 100); // Tree Trunk

  // Tree Leaves
  fill(0, 128, 0); // Green
  ellipse(x, y - 40, 80, 80); // Tree Leaves
}

void drawCloud(float x, float y) {
  // Cloud
  fill(255); // White
  ellipse(x, y, 80, 50);
  ellipse(x + 20, y - 20, 50, 50);
  ellipse(x + 40, y, 80, 50);
}

class Raindrop {
  float x, y;
  float speed;
  float length;

  Raindrop() {
    x = random(width);
    y = random(height);
    speed = random(2, 5); // Falling speed
    length = random(10, 20); // Length of raindrops
  }

  void fall() {
    y += speed;

    if (y > height) {
      y = random(-20, -10); // Reset raindrop position above the canvas
      x = random(width);
    }
  }

  void display() {
    stroke(0, 0, 255); // Blue raindrops
    line(x, y, x, y + length);
  }
}

class Bird {
  float x, y;
  float speedX; // Horizontal speed
  float speedY; // Vertical speed
  float wingAngle = 0; // Wing animation angle

  Bird(float x, float y) {
    this.x = x;
    this.y = y;
    speedX = random(1, 2);
    speedY = random(-0.5, 0.5);
  }

  void fly() {
    x += speedX;
    y += speedY;

    if (x > width) {
      x = -20;
      y = random(50, 150);
    }
  }

  void display() {
    // Bird Body
    fill(0); // Black
    ellipse(x, y, 20, 10); // Bird Body

    // Bird Wings (Two Triangles)
    fill(0); // Black
    pushMatrix();
    translate(x, y);
    rotate(radians(wingAngle));
    triangle(-10, 0, -20, -5, -10, -10); // Left Wing
    triangle(10, 0, 20, -5, 10, -10); // Right Wing
    popMatrix();

    // Animate wings
    wingAngle = sin(frameCount * 0.1) * 20;
  }
}
