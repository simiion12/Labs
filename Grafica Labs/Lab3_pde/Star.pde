class Star {
  PVector position;
  PVector velocity; // Velocity vector for movement
  float starSize;
  int starBrightness; // Grayscale color value
  boolean shouldMove; // Flag to determine if the star should move
  int sphereDetailLevel; // Sphere detail level

  Star(int detail) {
    position = PVector.random3D();
    position.mult(random(500)); // Adjust the range for star positions
    velocity = PVector.random3D();
    velocity.mult(random(0.3, 1)); // Adjust the speed of stars
    starSize = random(0.3, 3);   // Adjust the size range of stars
    starBrightness = int(random(200, 255)); // Adjust the brightness range (lighter)
    shouldMove = random(1) > 0.75; // 25% chance of moving
    sphereDetailLevel = detail; // Set the sphere detail level
  }

  void move() {
    if (shouldMove) {
      // Update star position based on velocity
      position.add(velocity);

      // Wrap stars around when they move off-screen
      if (position.x < -width / 2) position.x = width / 2;
      if (position.x > width / 2) position.x = -width / 2;
      if (position.y < -height / 2) position.y = height / 2;
      if (position.y > height / 2) position.y = -height / 2;
    }
  }

  void display() {
    pushMatrix();
    translate(position.x, position.y, position.z);
    fill(starBrightness); // Set the fill color to grayscale
    noStroke();
    sphereDetail(sphereDetailLevel); // Set the sphere detail level
    sphere(starSize);
    popMatrix();
  }
}
