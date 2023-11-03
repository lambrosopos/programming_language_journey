sfml-app: main.o
	g++ main.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system
main.o: main.cpp
	g++ -std=c++17 -c main.cpp -o main.o
run: sfml-app
	./sfml-app
clean:
	rm main.o sfml-app
