#include <string>
#include <SFML/Graphics.hpp>

const float wWidth = 400;
const float wHeight = 200;
const std::string wTitle = "SFML Works!";

// Only operate on transform components
void sMovement(std::vector<Entity>& entities) {
    for (auto& e : entities) {
        e.cTransform->pos += e.cTransform->velocity;
    }
}


void doStuff(std::vector<Entity>& entities) {
    for (auto& e : entities) {
        e.cTransform->pos += e.cTransform->velocity;
        e.cShape->shape.setPosition(e.cTransform->pos);
        window.draw(e.cShape->shape);
    }
}


// Main Game Loop with ECS
int main() {
    // Shared pointer will be false if not present
    std::vector<Entity> entities;
    Vec2 p(100, 200), v(10, 10);
    Entity e;
    e.cTransform = std::make_shared<Ctransform>(p, v);
    e.cName = std::make_shared<cName>("Red Box");
    e.cShape = std::make_shared<CShape> (args);

    entities.push_back(e);
    doStuff(entities);
}
