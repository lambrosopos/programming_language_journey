#include <string>
#include <SFML/Graphics.hpp>

const float wWidth = 400;
const float wHeight = 200;
const std::string wTitle = "SFML Works!";


void init() 
{
}

void update(sf::RenderWindow& window)
{
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
}

void draw(sf::RenderWindow& window, sf::CircleShape& shape)
{
        window.clear();
        window.draw(shape);
        window.display();
}

int main()
{
    sf::RenderWindow window(sf::VideoMode(wWidth, wHeight), wTitle);
    sf::CircleShape shape(100.f);
    sf::CircleShape shape_2(20.f);

    shape.setFillColor(sf::Color::Green);
    shape_2.setFillColor(sf::Color::Yellow);
    shape_2.setOutlineColor(sf::Color::Blue);
    shape_2.setPosition(wWidth / 2 - 20, wHeight / 2 - 20);

    while (window.isOpen())
    {
	update(window);
	draw(window, shape_2);

    }

    return 0;
}

