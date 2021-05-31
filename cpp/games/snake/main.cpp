#include <iostream>
using namespace std;

/* Games need 4 functions
 * 
 * Setup, Draw, Input, Logic
 */


bool gameOver;

// setup width and height -> dimensions for the game
const int width = 20;
const int height = 20;

// snake and fruit locations and the game score
int x, y, fruitX, fruitY, score;

// tracking directions


void Setup() {
  gameOver = false;
}

void Draw() {
}

void Input() {}

void Logic() {}

int main() 
{
  Setup();
  while (!gameOver) {
    Draw();
    Input();
    Logic();
  }
}
