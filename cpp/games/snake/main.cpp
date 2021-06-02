#include <iostream>
//#include <conio.h>
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
 
// enum is user-defined data type.
// only one value can be selected at a time
enum eDirection { STOP=0, LEFT, RIGHT, UP, DOWN } dir;


void Setup() {
    gameOver = false;

    // Initial direction snake moves is 0, 'STOP'
    dir = STOP;

    // Initial position is at the middle of the screen
    x = width / 2;
    y = height /2;

    fruitX = rand() % width;
    fruitY = rand() % height;

    score = 0;
}

void Draw() {
    // std::system to access system CLI
    system("clear");

    // printing top wall
    for (int i = 0; i < width; i++) {
        cout << '#';
    }

    cout << endl;

    // printing inner walls
    for (int i = 0; i < height - 2; i++) {
        for (int j = 0; j < width - 1; j++) {
            if (j == 0) {
                cout << '#';
            }

            if (i == y && j == x) {
                cout << "O";
            } else if (i == fruitY && j == fruitX) {
                cout << 'F';
            } else {
                cout << ' ';
            }

            if (j == width - 2) {
                cout << '#';
            }
        }
        cout << endl;

    }




    // printing bottom wall
    for (int i = 0; i < width; i++) {
        cout << '#';
    }

    cout << endl;
}

void Input() {
    // get keyboard input
    //if (_kbhit()) {
        // get key pressed
        //switch (_getch()) {
            //case 'a':
                //dir = LEFT;
                //break;
            //case 'w':
                //dir = UP;
                //break;
            //case 's':
                //dir = DOWN;
                //break;
            //case 'd':
                //dir = RIGHT;
                //break;
            //case 'x':
                //gameOver = true;
                //break;
        //}
    //}
}

void Logic() {
}

int main() 
{
    Setup();
    while (!gameOver) {
        Draw();
        Input();
        Logic();
    }
}
