# Python vs C++ Syntax Comparison

A comprehensive side-by-side comparison of Python and C++ syntax with examples.

---

## Table of Contents
1. [Basic Program Structure](#basic-program-structure)
2. [Variables and Data Types](#variables-and-data-types)
3. [Input/Output](#inputoutput)
4. [Conditional Statements](#conditional-statements)
5. [Loops](#loops)
6. [Functions](#functions)
7. [Arrays/Lists](#arrayslists)
8. [Classes and Objects](#classes-and-objects)
9. [Exception Handling](#exception-handling)
10. [File Operations](#file-operations)

---

## Basic Program Structure

### Python
```python
# Simple Hello World - WINNER
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

### C++
```cpp
// Simple Hello World - LOSER
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

---

## Variables and Data Types

### Python
```python
# Dynamic typing - no need to declare type - WINNER!
name = "John"           # string
age = 25               # int
height = 5.9           # float
is_student = True      # boolean
numbers = [1, 2, 3]    # list

# Type hints (optional) - WINNER!
name: str = "John"
age: int = 25

# Multiple assignment - CHICKEN DINNER!
x, y, z = 1, 2, 3

```

### C++
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Static typing - must declare type - LOSER!
string name = "John";
int age = 25;
double height = 5.9;
bool is_student = true;
vector<int> numbers = {1, 2, 3};

// Auto keyword (C++11+) - LOSER!
auto x = 42;        // int
auto y = 3.14;      // double
auto z = "hello";   // const char*

// Multiple declaration - LOSER!
int a = 1, b = 2, c = 3;
```

---

## Input/Output

### Python
```python
# Input - WINNER!
name = input("Enter name: ")
age = int(input("Enter age: "))

# Multiple values - WINNER!
print("Values:", x, y, z)
print(f"Sum: {x + y + z}")
```

### C++
```cpp
#include <iostream>
using namespace std;

// Input - LOSER!
cout << "Enter name: ";
cin >> name;
cout << "Enter age: ";
cin >> age;

// Multiple values - LOSER!
cout << "Values: " << x << " " << y << " " << z << endl;
cout << "Sum: " << (x + y + z) << endl;
```

---

## Conditional Statements

### Python
```python
# If-elif-else - TIE
if age < 18:
    pass
elif age < 65:
    pass
else:
    pass

# Ternary operator - WINNER
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions - WINNER
if age >= 18 and age < 65:

# Membership testing - WINNER
if name in ["John", "Jane", "Bob"]:
    print("Known person")
```

### C++
```cpp
// If-else if-else - TIE? NO PASS NEEDED IF EMPTY
if (age < 18) {
} else if (age < 65) {
} else {
}

// Ternary operator - TIE
string status = (age >= 18) ? "Adult" : "Minor";

// Multiple conditions - TIE
if (age >= 18 && age < 65) {
    cout << "Working age" << endl;
}

// Switch statement - WINNER FOR MANY COMPARISONS!
switch (grade) {
    case 'A':
        cout << "Excellent" << endl;
        break;
    case 'B':
        cout << "Good" << endl;
        break;
    default:
        cout << "Try harder" << endl;
}
```

---

## Loops

### Python
```python
# For loop with range - WINNER
for i in range(5):
    print(i)

# For loop with list - WINNER
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For loop with enumerate - WINNER
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loop - WINNER
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension - I LOVE 'EM
squares = [x**2 for x in range(10)]
```

### C++
```cpp
// For loop (traditional) - NOPE
for (int i = 0; i < 5; i++) {
    cout << i << endl;
}

// Range-based for loop (C++11+) - NOPE NOPE
vector<string> fruits = {"apple", "banana", "orange"};
for (const string& fruit : fruits) {
    cout << fruit << endl;
}

// For loop with index - WHAT?
for (size_t i = 0; i < fruits.size(); i++) {
    cout << i << ": " << fruits[i] << endl;
}

// While loop - TIE, KIND OF
int count = 0;
while (count < 5) {
    count++;
}

// Do-while loop - OK
do {
    count++;
} while (count < 10);
```

---

## Functions

### Python
```python
# Basic function - ~OK A TIE
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters - WINNER
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple return values - CHICKEN DINNER
def get_name_age():
    return "John", 25

# Lambda function - WINNER
square = lambda x: x**2

# Function with *args and **kwargs - WINNER
def flexible_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Call examples - WINNER
message = greet("Alice")
name, age = get_name_age()
result = square(5)
flexible_function(1, 2, 3, name="John", age=25)
```

### C++
```cpp
#include <iostream>
#include <string>
using namespace std;

// Basic function = TIE
string greet(string name) {
    return "Hello, " + name + "!";
}

// Function with default parameters - TIE
string greetWithTitle(string name, string title = "Mr.") {
    return "Hello, " + title + " " + name + "!";
}

// Function with reference parameters - 
void increment(int& value) {
    value++;
}

// Function overloading - BUNCH OF LOSERS
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

// Lambda function (C++11+) - LOSER
auto square = [](int x) { return x * x; };

// Call examples - NOPALOPE
int main() {
    string message = greet("Alice");
    int num = 5;
    increment(num);  // num becomes 6
    int result = square(5);
    return 0;
}
```

---

## Arrays/Lists

### Python
```python
# Lists (dynamic arrays) - WINNER
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations - WINNER
numbers.append(6)           # Add element
numbers.insert(0, 0)        # Insert at index
numbers.remove(3)           # Remove specific value
popped = numbers.pop()      # Remove and return last
length = len(numbers)       # Get length

# List slicing - WINNER
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]

# List comprehension - WINNER
squares = [x**2 for x in range(1, 6)]
evens = [x for x in numbers if x % 2 == 0]
```

### C++
```cpp
#include <vector>
#include <array>
#include <iostream>
using namespace std;

// Static array - ONLY ONE TYPE? DECLARE SIZE?
int static_arr[5] = {1, 2, 3, 4, 5};

// std::array (C++11+)
array<int, 5> std_arr = {1, 2, 3, 4, 5};

// std::vector (dynamic array) - CLOSER BUT ONLY INT?
vector<int> numbers = {1, 2, 3, 4, 5};

// Vector operations - MEH
numbers.push_back(6);              // Add element
numbers.insert(numbers.begin(), 0); // Insert at beginning
numbers.erase(numbers.begin() + 2);  // Remove at index 2
int last = numbers.back();           // Get last element
numbers.pop_back();                  // Remove last element
size_t length = numbers.size();      // Get size

// Accessing elements
for (int i = 0; i < numbers.size(); i++) {
    cout << numbers[i] << " ";
}

// Range-based loop
for (int num : numbers) {
    cout << num << " ";
}
```

---

## Classes and Objects

### Python
```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

    # Class method
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Inheritance
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    
    def study(self):
        return f"{self.name} is studying at {self.school}"

# Usage
person = Person("Alice", 25)
student = Student("Bob", 20, "MIT")
print(person.introduce())
print(student.study())
```

### C++
```cpp
#include <iostream>
#include <string>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    // Static member
    static string species;
    
    // Constructor
    Person(string n, int a) : name(n), age(a) {}
    
    // Destructor - LOSER
    ~Person() {
        cout << "Person destructor called" << endl;
    }
    
    // Member function
    string introduce() {
        return "Hi, I'm " + name + " and I'm " + to_string(age) + " years old";
    }
    
    // Static function
    static bool isAdult(int age) {
        return age >= 18;
    }
    
    // Getters/Setters
    string getName() const { return name; }
    void setName(string n) { name = n; }
};

// Initialize static member
string Person::species = "Homo sapiens";

// Inheritance
class Student : public Person {
private:
    string school;

public:
    Student(string n, int a, string s) : Person(n, a), school(s) {}
    
    string study() {
        return getName() + " is studying at " + school;
    }
};

// Usage
int main() {
    Person person("Alice", 25);
    Student student("Bob", 20, "MIT");
    cout << person.introduce() << endl;
    cout << student.study() << endl;
    return 0;
}
```

---

## Exception Handling

### Python
```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup code here")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### C++
```cpp
#include <iostream>
#include <stdexcept>
using namespace std;

// Basic try-catch
try {
    int result = 10 / 0;  // This won't throw in C++, but for example
} catch (const exception& e) {
    cout << "Error: " << e.what() << endl;
}

// Multiple catch blocks
try {
    // Some risky operation
    throw runtime_error("Something went wrong");
} catch (const runtime_error& e) {
    cout << "Runtime error: " << e.what() << endl;
} catch (const exception& e) {
    cout << "General error: " << e.what() << endl;
} catch (...) {
    cout << "Unknown error occurred" << endl;
}

// Custom exception
class AgeException : public exception {
public:
    const char* what() const noexcept override {
        return "Invalid age provided";
    }
};

// Function that throws
int validateAge(int age) {
    if (age < 0) {
        throw AgeException();
    }
    return age;
}
```

---

## File Operations - RELATIVE TIE

### Python
```python
# Writing to file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python file operations")

# Reading from file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to file
with open("example.txt", "a") as file:
    file.write("\nAppended text")

# Reading all lines into list
with open("example.txt", "r") as file:
    lines = file.readlines()

# Exception handling with files
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

### C++
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Writing to file
ofstream outFile("example.txt");
if (outFile.is_open()) {
    outFile << "Hello, World!" << endl;
    outFile << "C++ file operations" << endl;
    outFile.close();
}

// Reading from file
ifstream inFile("example.txt");
if (inFile.is_open()) {
    string line;
    while (getline(inFile, line)) {
        cout << line << endl;
    }
    inFile.close();
}

// Reading entire file
ifstream file("example.txt");
if (file.is_open()) {
    string content;
    string line;
    while (getline(file, line)) {
        content += line + "\n";
    }
    cout << content << endl;
    file.close();
}

// Appending to file
ofstream appendFile("example.txt", ios::app);
if (appendFile.is_open()) {
    appendFile << "Appended text" << endl;
    appendFile.close();
}

// Error checking
ifstream checkFile("nonexistent.txt");
if (!checkFile.is_open()) {
    cout << "File not found!" << endl;
}
```

---

## Key Differences Summary

| Feature | Python | C++ |
|---------|--------|-----|
| **Typing** | Dynamic | Static |
| **Memory Management** | Automatic (Garbage Collection) | Manual (new/delete) or Smart Pointers |
| **Compilation** | Interpreted | Compiled |
| **Syntax** | Indentation-based | Brace-based |
| **Performance** | Slower (interpreted) | Faster (compiled) |
| **Learning Curve** | Easier | Steeper |
| **Use Cases** | Scripting, Data Science, Web | System Programming, Games, Performance-critical |

---

*This comparison covers the most common syntax patterns. Both languages have many more advanced features and libraries available.*