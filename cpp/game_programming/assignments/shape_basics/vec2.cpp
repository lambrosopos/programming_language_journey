#include <iostream>
#include <math.h>

class Vec2 {
    public:
        float x = 0;
        float y = 0;

        Vec2() {}
        Vec2(float xin, float yin) : x(xin), y(yin) {}

        Vec2 operator + (Vec2 v) {
            return Vec2(x + v.x, y + v.y);
        }

        Vec2 operator - (Vec2 v) {
            return Vec2(x - v.x, y - v.y);
        }

        Vec2 operator * (float s) {
            return Vec2(x * s, y * s);
        }

        bool operator == (Vec2 v) {
            return (v.x == x) && (v.y == y);
        }

        float length() {
            return sqrtf((x*x) + (y*y));
        }

        float dist(Vec2 v) {
            return (v-*this).length();
        }
};

int main(int argc, char* argv[]) {
    Vec2 v1(100, 100);
    Vec2 v2(200, 100);

    float dist = v1.dist(v2);
    std::cout << dist << "\n";
    return 0;
}

