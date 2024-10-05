// Declare global variables
float xOff = 0;          // X offset for Perlin noise
float yOff = 1000;       // Y offset for Perlin noise
float stepSize = 10;     // Incremental angle for drawing lines
float maxRadius = 300;   // Maximum radius for circles

// Setup function runs once at the beginning
void setup() {
  size(800, 800);         // Set up a canvas of size 800x800 pixels
  background(255);        // Set the background color to white
  noFill();               // Don't fill shapes
  stroke(0, 50);          // Set stroke color to black with alpha (transparency) of 50
  randomSeed(42);         // Set a random seed for consistent randomness
  noiseSeed(42);          // Set a noise seed for consistent Perlin noise
  noiseDetail(4, 0.5);    // Set noise detail and falloff
}

// Draw function runs continuously
void draw() {
  float xPrev = -1;       // Initialize previous x coordinate
  float yPrev = -1;       // Initialize previous y coordinate
  
  // Loop through angles from 0 to 2π with a step of 5 degrees
  for (float a = 0; a < TWO_PI; a += radians(5)) {
    // Calculate radius using Perlin noise
    float rad = maxRadius * noise(xOff, yOff);
    
    // Calculate coordinates of a point on a circle
    float x = width / 2 + cos(a) * rad;
    float y = height / 2 + sin(a) * rad;
    
    // Check if there's a previous point
    if (xPrev > 0 && yPrev > 0) {
      // Map radius to transparency values
      float alpha = map(rad, 0, maxRadius, 50, 255);
      
      // Set stroke color with adjusted transparency
      stroke(0, alpha);
      
      // Draw a line from the previous point to the current point
      line(xPrev, yPrev, x, y);
    }
    
    // Update previous coordinates
    xPrev = x;
    yPrev = y;
    
    // Increment X offset for Perlin noise
    xOff += 0.1;
  }
  
  // Increment Y offset for Perlin noise
  yOff += 0.01;
  
  // Check if the frame count is 400 and stop looping to freeze the animation
  if (frameCount == 400) {
    noLoop();
  }
}
