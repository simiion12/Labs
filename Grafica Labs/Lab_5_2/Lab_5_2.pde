Creature creature;

void setup() {
  size(800, 600);
  creature = new Creature(width / 2, height / 2, 50, 0.02, 50); // 6 wings
}

void draw() {
  background(224,158,118);
  creature.update();
  creature.display();
}

void keyPressed() {
  if (keyCode == UP) {
    creature.setDirection(0, -1);
  } else if (keyCode == DOWN) {
    creature.setDirection(0, 1);
  } else if (keyCode == LEFT) {
    creature.setDirection(-1, 0);
  } else if (keyCode == RIGHT) {
    creature.setDirection(1, 0);
  } else if (key == 'B' || key == 'b') {
    creature.changeSize(1.1); // Increase size
  } else if (key == 'S' || key == 's') {
    creature.changeSize(0.9); // Decrease size
  }
}

void keyReleased() {
  creature.setDirection(0, 0);
}

class Creature {
  PVector center;
  float radius;
  float angle;
  float angleVelocity;
  float speed;
  PVector acceleration;
  PVector velocity;
  PVector direction;
  ArrayList<Wings> wingsList;

  Creature(float x, float y, float radius, float angleVelocity, int numWings) {
    center = new PVector(x, y);
    this.radius = radius;
    this.angle = 0;
    this.angleVelocity = angleVelocity;
    this.speed = 2;
    this.acceleration = new PVector(0.1, 0.1);
    this.velocity = new PVector(this.speed, 0);
    this.direction = new PVector(0, 0);
    wingsList = new ArrayList<Wings>();

    for (int i = 0; i < numWings; i++) {
      wingsList.add(new Wings());
    }
  }

  void update() {
    // Update speed based on acceleration
    this.speed += this.acceleration.mag();

    // Update position based on speed and direction
    this.velocity.set(this.direction.x * this.speed, this.direction.y * this.speed);
    this.center.add(this.velocity);

    // Oscillate the angle of the creature's wings based on speed
    this.angle += this.speed * this.angleVelocity;

    // Update wings position
    for (Wings wings : wingsList) {
      wings.update(this.center, this.angle);
    }

    // Check boundaries and reverse direction if needed
    if (this.center.x > width - this.radius) {
      this.center.x = width - this.radius;
    } else if (this.center.x < this.radius) {
      this.center.x = this.radius;
    }

    if (this.center.y > height - this.radius) {
      this.center.y = height - this.radius;
    } else if (this.center.y < this.radius) {
      this.center.y = this.radius;
    }
  }

  void display() {
    // Draw the creature
    pushMatrix();
    translate(this.center.x, this.center.y);

    // Draw body
    ellipse(0, 0, this.radius * 2, this.radius * 2);

    // Draw eyes
    fill(216,240,232);
    ellipse(-10, -10, 10, 10);
    ellipse(10, -10, 10, 10);
    

    // Draw smile
    arc(0, 5, 30, 20, 0, PI);
    fill(133,122,106);

    // Draw wings
    for (Wings wings : wingsList) {
      wings.display(this.radius); // Pass the radius to the display method
    }

    popMatrix();
  }

  void setDirection(float x, float y) {
    direction.set(x, y);
  }

  void changeSize(float scaleFactor) {
    this.radius *= scaleFactor;
    for (Wings wings : wingsList) {
      wings.changeSize(scaleFactor);
    }
  }
}

class Wings {
  float wingLength;
  float oscillationAmplitude;
  float wingAngleOffset;

  Wings() {
    wingLength = 30;
    oscillationAmplitude = 20;
    wingAngleOffset = random(TWO_PI); // Randomize initial wing angles
  }

  void update(PVector center, float angle) {
    // Wings update logic, if needed
  }

  void display(float creatureRadius) {
    // Oscillate wings
    float wingOscillation = sin(frameCount * 0.05 + wingAngleOffset) * oscillationAmplitude;

    // Draw wings
    line(creatureRadius, 0, creatureRadius + wingLength, wingOscillation);
    line(-creatureRadius, 0, -creatureRadius - wingLength, wingOscillation);
  }

  void changeSize(float scaleFactor) {
    this.wingLength *= scaleFactor;
    this.oscillationAmplitude *= scaleFactor;
  }
}
