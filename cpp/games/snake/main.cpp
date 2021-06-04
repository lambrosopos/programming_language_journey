#include <iostream>
#include <ncurses.h>

using namespace std;

/* Games need 4 functions
 * 
 * Setup, Draw, Input, Logic
 */


bool gameOver;

// setup width and height -> dimensions for the game
const int width = 20;
const int height = 10;

// snake and fruit locations and the game score
int x, y, fruitX, fruitY, score;
// tracking directions
 
// enum is user-defined data type.
// only one value can be selected at a time
enum eDirection { STOP=0, LEFT, RIGHT, UP, DOWN };
eDirection dir;


void Setup() {
    initscr();
    clear();
    noecho();
    cbreak();
    curs_set(0);

    gameOver = false;

    // Initial direction snake moves is 0, 'STOP'
    dir = STOP;

    // Initial position is at the middle of the screen
    x = width / 2;
    y = height /2;

    fruitX = (rand() % width) + 1;
    fruitY = (rand() % height) + 1;

    score = 0;
}

void Draw() {
    // std::system to access system CLI
    clear();

    // printing top wall
    for (int i = 0; i < width + 2; i++)
        mvprintw(0, 1, "+");

    for (int i = 0; i < height + 2; i++)
    {
        for (int j = 0; j < width + 2; j++)
        {
            if (i == 0 | i == 21)
                mvprintw(i, j, "+");
            else if (j== 0 | j == 21)
                mvprintw(i, j, "+");
            else if (i == y && j == x)
                mvprintw(i, j, "O");
            else if (i == fruitY && j == fruitX)
                mvprintw(i, j, "@");
        }
    }
    mvprintw(23, 0, "Score %d", score);

    refresh();
    getch();
    endwin();

}

void Input() {
    // get keyboard input
    char inputChar;
    cout << "what the heck =================";
    cin >> inputChar;

    cout << inputChar << endl;

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
    Draw();
    //while (!gameOver) {
        //Draw();
        //Input();
        //Logic();
    //}
    return 0;
}
