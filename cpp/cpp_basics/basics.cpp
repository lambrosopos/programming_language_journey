//
//  main.cpp
//  c_basics
//
//  Created by San Kim on 2021/05/19.
//

#include <iostream>

using namespace std;

//int main()
//{
//    string characterName = "John";
//    int characterAge;
//    characterAge = 35;
//    cout << "There once was a man named " << characterName << endl;
//    cout << "He was " << characterAge << " years old" << endl;
//    cout << "He liked the name " << characterName << endl;
//    cout << "But did not like being " << characterAge << endl;
//}

// variable types
//int main()
//{
//    // character
//    char grade = 'A';
//
//    cout << grade << endl;
//
//    // string is a bunch of characters
//    // you need to use " not '
//    string phrase = "Hello";
//
//    cout << phrase << endl;
//
//    // integers can't have decimals
//    int age = -50;
//
//    // decimals are represented by 2 basic types
//    float weight = -12.3;
//
//    // double stores more decimal points than a float
//    double extra_weight = -59.22249;
//
//    cout << age << weight << extra_weight << endl;
//
//    // boolean
//    bool is_human = true;
//
//    cout << is_human << endl;
//}

// working with strings
//int main()
//{
//    string phrase = "Hello world";
//    //index          012345678910
//    cout << "phrase: " << phrase << endl;
//    cout << "phrase.length(): " << phrase.length() << endl;
//    cout << "phrase[0]: " << phrase[0] << endl;
//    cout << "phrase.find(): " << phrase.find("World", 0) << endl;
//    cout << "phrase.substr(0, 4): " << phrase.substr(0, 4) << endl;
//    string phrase_sub = phrase.substr(4, 1);
//    cout << "phrase.substr(4, 1): " << phrase_sub << endl;
//
//    return 0;
//}

#include <cmath>
// numbers in c
//int main()
//{
//    // doubles allow more decimal points in a float
//    cout << "15 + 5: " << 15 + 5 << endl;
//
//    // modulus operator
//    cout << "10 % 3: " << 10 % 3 << endl;
//
//    int wnum = 5;
//    double dnum = 5.5;
//
//    cout << "double: " << dnum << endl;
//
//    wnum++;
//
//    cout << "wnum++: " << wnum << endl;
//
//    // integer and decimal gives back decimal
//    // except math with integers, all values will return decimals
//    cout << "5.5 + 9: " << 5.5 + 9 << endl;
//
//    // basic math functions
//    // you need <cmath>
//
//    cout << "pow(4, 2): " << pow(4, 2) << endl;
//    cout << "sqrt(36): " << sqrt(36) << endl;
//    cout << "round(4.32): " << round(4.32) << endl;
//    cout << "round(4.82): " << round(4.82) << endl;
//    cout << "fmax(10.3, 10.2): " << fmax(10.3, 10.2) << endl;
//
//    return 0;
//}


// getting user input
//int main()
//{
//    int age;
//    cout << "Enter your age: ";
//    cin >> age;
//
//    cout << "Your age is: " << age << endl;
//
//    string name;
//    cout << "Enter your name: ";
//    getline(cin, name);
//
//    cout << "Your name is: " << name << endl;
//
//    return 0;
//}

// basic calculator
//int main()
//{
//    double num1, num2;
//    cout << "First number: ";
//    cin >> num1;
//
//    cout << "Second number: ";
//    cin >> num2;
//
//    cout << "num1 + num2: " << num1 + num2 << endl;
//
//    return 0;
//}

// madlibs
//int main()
//{
//    string color, pluralNoun, celebrity;
//
//    cout << "enter a color: ";
//    getline(cin, color);
//
//    cout << "enter a plural noun: ";
//    getline(cin, pluralNoun);
//
//    cout << "enter a celebrity: ";
//    getline(cin, celebrity);
//
//    cout << "Roses are " + color << endl;
//    cout << pluralNoun << " are blue" << endl;
//    cout << "I love " << celebrity << endl;
//
//    return 0;
//}

// arrays in c++
//int main()
//{
//    int luckyNums[] = {4, 8, 15, 16, 23, 42};
//    // index:          0  1   2   3   4   5
//
//    cout << "luckyNums: " << luckyNums << endl;
//    cout << "luckyNums[0]: " << luckyNums[0] << endl;
//
//    luckyNums[0] = 8;
//    cout << "luckyNums[0]: " << luckyNums[0] << endl;
//
//    // giving arrays a size
//    int fixedLuckyNums[20] = {4, 8, 15, 16, 23, 42};
//
//    fixedLuckyNums[20] = 22;
//
//    cout << "fixedLuckyNums[20]: " << fixedLuckyNums[20] << endl;
//
//    return 0;
//}

// functions in c++

// functions need information:
//  1. return type

// functions need to know each others' existence

//void sayHi(string name);
//
//int main()
//{
//    // purpose of main function is to be executed when file is run
//    sayHi("robo");
//    return 0;
//}
//
//void sayHi(string name) {
//    cout << "Hello user: " << name << endl;
//}

