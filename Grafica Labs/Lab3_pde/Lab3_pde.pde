import peasy.*; // Import the Peasy library for easy camera control

Planet sun; // Declare a variable for the sun (a planet)
PeasyCam cam; // Declare a variable for camera control
PImage sunTexture; // Texture for the sun
PImage[] textures = new PImage[4]; // Array of textures for planets
Star[] stars = new Star[250]; // Array to store star objects

void setup() {
  size(600, 600, P3D); // Create a 3D canvas
  sunTexture = loadImage("sun.jpg"); // Load the sun texture image
  textures[0] = loadImage("earth.jpg"); // Load textures for other planets
  textures[1] = loadImage("jupiter.jpg");
  textures[2] = loadImage("mars.jpg");
  textures[3] = loadImage("neptune.jpg");
  cam = new PeasyCam(this, 500); // Create a PeasyCam for easy 3D camera control
  sun = new Planet(50, 0, 0, sunTexture); // Create the sun (a planet) with a radius of 50 and no initial orbit
  sun.spawnMoons(4, 1); // Spawn moons for the sun
  for (int i = 0; i < stars.length; i++) {
    int detail = int(random(3, 10)); // Generate a random detail level for stars
    stars[i] = new Star(detail); // Create a star with the specified detail level
  }
}

void draw() {
  background(0); // Set the background color to black
  lights(); // Enable lighting and shading

  for (Star star : stars) {
    star.move(); // Move the stars
    star.display(); // Display the stars
  }

  sun.show(); // Display the sun and its moons
  sun.orbit(); // Update the position of the sun in its orbit
}
