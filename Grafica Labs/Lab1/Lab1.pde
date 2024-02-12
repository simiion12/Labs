void setup() {
size(400, 400);
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

// Door
fill(139, 69, 19); // Brown
rect(220, 260, 40, 40); // Door

// Trees
drawTree(50, 250);
drawTree(120, 280);
drawTree(280, 280);
drawTree(350, 250);

// Birds
drawBird(50, 80);
drawBird(100, 120);
drawBird(200, 60);
drawBird(300, 100);
}

void drawTree(float x, float y) {
// Tree Trunk
fill(139, 69, 19); // Brown
rect(x - 10, y, 20, 100); // Tree Trunk

// Tree Leaves
fill(0, 128, 0); // Green
ellipse(x, y - 40, 80, 80); // Tree Leaves
}

void drawBird(float x, float y) {
// Bird Body
fill(0); // Black
ellipse(x, y, 20, 10); // Bird Body

// Bird Wings (Two Triangles)
fill(0); // Black
triangle(x - 10, y, x - 20, y - 5, x - 10, y - 10); // Left Wing
triangle(x + 10, y, x + 20, y - 5, x + 10, y - 10); // Right Wing
}
