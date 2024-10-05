class Planet {
  float radius;      // Radius of the planet
  float angle;       // Current angle in its orbit
  float distance;    // Distance from its parent planet
  Planet[] planets;  // Array to store its moons
  float orbitSpeed;  // Speed of the planet's orbit
  PVector v;         // Vector to store its position in 3D space
  
  PShape globe;      // 3D shape to represent the planet's surface
  
  // Constructor for creating a planet
  Planet(float r, float d, float o, PImage img) {
    v = PVector.random3D();
    radius = r;
    distance = d;
    v.mult(distance);
    angle = random(TWO_PI);
    orbitSpeed = o;
    
    noStroke();
    noFill();
    globe = createShape(SPHERE, radius); // Create a sphere shape with the given radius
    globe.setTexture(img);                // Apply a texture to the sphere
  }
  
  // Function to update the planet's position in its orbit
  void orbit() {
    angle = angle + orbitSpeed;
    if (planets != null) {
      for (int i = 0; i < planets.length; i++) {
        planets[i].orbit();
      }
    }
  }
  
  // Function to create moons for the planet
  void spawnMoons(int total, int level) {
    planets = new Planet[total];
    for (int i = 0; i < planets.length; i++) {
      float r = radius / (level * 2);     // Moon radius
      float d = random(75, 300);          // Moon distance from its parent
      float o = random(-0.06, 0.06);      // Moon's orbit speed
      int index = int(random(0, textures.length)); // Select a texture
      planets[i] = new Planet(r, d, o, textures[index]); // Create a moon
      if (level < 2) {
        int num = int(random(0, 4));      // Number of moons for this moon
        planets[i].spawnMoons(num, level + 1);
      }
    }
  }
  
  // Function to display the planet and its moons
  void show() {
    pushMatrix(); // Save the current transformation state
    noStroke();
    
    PVector v2 = new PVector(1, 0, 1);     // A vector for rotation
    PVector p = v.cross(v2);              // Compute the cross product for rotation
    rotate(angle, p.x, p.y, p.z);         // Rotate the planet
    translate(v.x, v.y, v.z);            // Translate to the planet's position
    fill(255);                            // Fill color for the planet
    shape(globe);                         // Display the planet's globe shape
    if (planets != null) {
      for (int i = 0; i < planets.length; i++) {
        planets[i].show();               // Recursively display moons
      }
    }
    popMatrix(); // Restore the previous transformation state
  }
}
