# Python vs Java Syntax Comparison

A comprehensive side-by-side comparison of Python and Java syntax with examples.

---

## Table of Contents
1. [Basic Program Structure](#basic-program-structure)
2. [Variables and Data Types](#variables-and-data-types)
3. [Input/Output](#inputoutput)
4. [Conditional Statements](#conditional-statements)
5. [Loops](#loops)
6. [Functions/Methods](#functionsmethods)
7. [Arrays/Lists](#arrayslists)
8. [Classes and Objects](#classes-and-objects)
9. [Exception Handling](#exception-handling)
10. [File Operations](#file-operations)
11. [Collections and Data Structures](#collections-and-data-structures)

---

## Basic Program Structure

### Python
```python
# Simple Hello World
print("Hello, World!")

# With main function
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()

# Module-level code runs immediately
x = 10
print(f"Value of x: {x}")
```

### Java
```java
// Simple Hello World
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

// With separate method
public class HelloWorld {
    public static void hello() {
        System.out.println("Hello, World!");
    }
    
    public static void main(String[] args) {
        hello();
    }
}

// Instance variables and methods
public class HelloWorld {
    private int x = 10;
    
    public void displayValue() {
        System.out.println("Value of x: " + x);
    }
    
    public static void main(String[] args) {
        HelloWorld obj = new HelloWorld();
        obj.displayValue();
    }
}
```

---

## Variables and Data Types

### Python
```python
# Dynamic typing - no need to declare type
name = "John"           # string
age = 25               # int
height = 5.9           # float
is_student = True      # boolean
numbers = [1, 2, 3]    # list

# Type hints (optional)
name: str = "John"
age: int = 25

# Multiple assignment
x, y, z = 1, 2, 3

# Constants (by convention)
PI = 3.14159
MAX_SIZE = 100

# None type
result = None

# Dynamic reassignment
variable = 42
variable = "Now I'm a string"
variable = [1, 2, 3]
```

### Java
```java
// Static typing - must declare type
String name = "John";
int age = 25;
double height = 5.9;
boolean isStudent = true;
int[] numbers = {1, 2, 3};

// Final variables (constants)
final double PI = 3.14159;
final int MAX_SIZE = 100;

// Object types
String text = "Hello";
Integer boxedInt = 42;

// Null reference
String result = null;

// Type inference (Java 10+)
var autoName = "John";      // String
var autoAge = 25;           // int
var autoHeight = 5.9;       // double

// Primitive vs Object types
int primitiveInt = 42;
Integer objectInt = 42;

// Array declaration variations
int[] array1 = new int[5];
int[] array2 = {1, 2, 3, 4, 5};
int[] array3 = new int[]{1, 2, 3, 4, 5};
```

---

## Input/Output

### Python
```python
# Output
print("Hello")
print("Name:", name)
print(f"Age: {age}")  # f-string formatting
print("Sum: {}".format(x + y))  # format method

# Input
name = input("Enter name: ")
age = int(input("Enter age: "))

# Multiple values
print("Values:", x, y, z)
print(f"Sum: {x + y + z}")

# Print with different separators/endings
print("A", "B", "C", sep="-")
print("No newline", end="")
print(" continues here")
```

### Java
```java
import java.util.Scanner;

public class InputOutput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Output
        System.out.println("Hello");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.printf("Age: %d%n", age);  // printf formatting
        
        // Input
        System.out.print("Enter name: ");
        String name = scanner.nextLine();
        System.out.print("Enter age: ");
        int age = scanner.nextInt();
        
        // Multiple values
        System.out.println("Values: " + x + " " + y + " " + z);
        System.out.println("Sum: " + (x + y + z));
        
        // Different output methods
        System.out.print("No newline");
        System.out.println(" continues here");
        System.err.println("Error message");
        
        scanner.close();
    }
}
```

---

## Conditional Statements

### Python
```python
# If-elif-else
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
if age >= 18 and age < 65:
    print("Working age")

# Membership testing
if name in ["John", "Jane", "Bob"]:
    print("Known person")

# Chained comparisons
if 0 <= score <= 100:
    print("Valid score")

# Boolean evaluation
if items:  # True if list is not empty
    print("Has items")
```

### Java
```java
// If-else if-else
if (age < 18) {
    System.out.println("Minor");
} else if (age < 65) {
    System.out.println("Adult");
} else {
    System.out.println("Senior");
}

// Ternary operator
String status = (age >= 18) ? "Adult" : "Minor";

// Multiple conditions
if (age >= 18 && age < 65) {
    System.out.println("Working age");
}

// Switch statement
switch (grade) {
    case 'A':
        System.out.println("Excellent");
        break;
    case 'B':
        System.out.println("Good");
        break;
    case 'C':
        System.out.println("Average");
        break;
    default:
        System.out.println("Try harder");
}

// Switch expression (Java 14+)
String result = switch (grade) {
    case 'A' -> "Excellent";
    case 'B' -> "Good";
    case 'C' -> "Average";
    default -> "Try harder";
};

// Boolean evaluation
if (list != null && !list.isEmpty()) {
    System.out.println("Has items");
}
```

---

## Loops

### Python
```python
# For loop with range
for i in range(5):
    print(i)

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For loop with enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Loop control
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

### Java
```java
import java.util.*;

// Traditional for loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// Enhanced for loop (for-each)
String[] fruits = {"apple", "banana", "orange"};
for (String fruit : fruits) {
    System.out.println(fruit);
}

// For loop with index
for (int i = 0; i < fruits.length; i++) {
    System.out.println(i + ": " + fruits[i]);
}

// While loop
int count = 0;
while (count < 5) {
    System.out.println(count);
    count++;
}

// Do-while loop
do {
    System.out.println(count);
    count++;
} while (count < 10);

// Stream operations (Java 8+)
List<Integer> squares = IntStream.range(0, 10)
    .map(x -> x * x)
    .boxed()
    .collect(Collectors.toList());

List<Integer> evens = IntStream.range(0, 20)
    .filter(x -> x % 2 == 0)
    .boxed()
    .collect(Collectors.toList());

// Nested loops
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        System.out.println("(" + i + ", " + j + ")");
    }
}

// Loop control
for (int i = 0; i < 10; i++) {
    if (i == 3) continue;
    if (i == 7) break;
    System.out.println(i);
}
```

---

## Functions/Methods

### Python
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple return values
def get_name_age():
    return "John", 25

# Function with *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

# Lambda function
square = lambda x: x**2
add = lambda x, y: x + y

# Higher-order functions
def apply_operation(x, y, operation):
    return operation(x, y)

# Decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@timing_decorator
def slow_function():
    return "Done"

# Call examples
message = greet("Alice")
name, age = get_name_age()
result = square(5)
flexible_function(1, 2, 3, name="John", age=25)
sum_result = apply_operation(3, 4, add)
```

### Java
```java
import java.util.function.*;

public class Functions {
    // Basic method
    public static String greet(String name) {
        return "Hello, " + name + "!";
    }
    
    // Method with default-like behavior using overloading
    public static String greetWithTitle(String name) {
        return greetWithTitle(name, "Mr.");
    }
    
    public static String greetWithTitle(String name, String title) {
        return "Hello, " + title + " " + name + "!";
    }
    
    // Method with varargs
    public static void flexibleFunction(String... args) {
        System.out.println("Args: " + Arrays.toString(args));
    }
    
    // Generic method
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
    
    // Functional interfaces (Java 8+)
    Function<Integer, Integer> square = x -> x * x;
    BinaryOperator<Integer> add = (x, y) -> x + y;
    
    // Higher-order method
    public static int applyOperation(int x, int y, BinaryOperator<Integer> operation) {
        return operation.apply(x, y);
    }
    
    // Method returning multiple values using custom class
    public static class NameAge {
        public final String name;
        public final int age;
        
        public NameAge(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }
    
    public static NameAge getNameAge() {
        return new NameAge("John", 25);
    }
    
    public static void main(String[] args) {
        String message = greet("Alice");
        NameAge result = getNameAge();
        int squared = square.apply(5);
        flexibleFunction("a", "b", "c");
        int sumResult = applyOperation(3, 4, add);
    }
}
```

---

## Arrays/Lists

### Python
```python
# Lists (dynamic arrays)
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
numbers.append(6)           # Add element
numbers.insert(0, 0)        # Insert at index
numbers.remove(3)           # Remove specific value
popped = numbers.pop()      # Remove and return last
length = len(numbers)       # Get length

# List slicing
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]
reversed_list = numbers[::-1]

# List methods
numbers.extend([7, 8, 9])   # Add multiple elements
numbers.sort()              # Sort in place
sorted_copy = sorted(numbers)  # Return sorted copy
numbers.reverse()           # Reverse in place

# List comprehension
squares = [x**2 for x in range(1, 6)]
evens = [x for x in numbers if x % 2 == 0]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Java
```java
import java.util.*;

// Arrays (fixed size)
int[] numbers = {1, 2, 3, 4, 5};
int[] staticArray = new int[5];

// ArrayList (dynamic)
ArrayList<Integer> list = new ArrayList<>();
ArrayList<Integer> listWithValues = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));

// List operations
list.add(6);                    // Add element
list.add(0, 0);                 // Insert at index
list.remove(Integer.valueOf(3)); // Remove specific value
list.remove(0);                 // Remove at index
int popped = list.remove(list.size() - 1);  // Remove last
int length = list.size();       // Get size

// Array operations
int arrayLength = numbers.length;
Arrays.sort(numbers);           // Sort array
int[] copy = Arrays.copyOf(numbers, numbers.length);

// List methods
List<Integer> moreNumbers = Arrays.asList(7, 8, 9);
list.addAll(moreNumbers);       // Add multiple elements
Collections.sort(list);         // Sort list
Collections.reverse(list);      // Reverse list

// Stream operations (Java 8+)
List<Integer> squares = list.stream()
    .map(x -> x * x)
    .collect(Collectors.toList());

List<Integer> evens = list.stream()
    .filter(x -> x % 2 == 0)
    .collect(Collectors.toList());

// 2D arrays
int[][] matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
int[][] dynamicMatrix = new int[3][3];

// List of Lists
List<List<Integer>> listMatrix = new ArrayList<>();
listMatrix.add(Arrays.asList(1, 2, 3));
listMatrix.add(Arrays.asList(4, 5, 6));
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
        self._protected = "protected"
        self.__private = "private"
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    # Property with getter/setter
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    # Class method
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    # String representation
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Inheritance
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
    
    def study(self):
        return f"{self.name} is studying at {self.school}"
    
    # Method overriding
    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} and I study at {self.school}"

# Multiple inheritance
class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def work(self):
        return "Working..."

class WorkingStudent(Student, Employee):
    def __init__(self, name, age, school, salary):
        Student.__init__(self, name, age, school)
        Employee.__init__(self, salary)

# Usage
person = Person("Alice", 25)
student = Student("Bob", 20, "MIT")
worker = WorkingStudent("Charlie", 22, "Harvard", 50000)
```

### Java
```java
// Base class
public class Person {
    // Class variable
    public static final String SPECIES = "Homo sapiens";
    
    // Instance variables
    private String name;
    private int age;
    protected String protectedField;
    
    // Constructor
    public Person(String name, int age) {
        this.name = name;
        setAge(age);  // Use setter for validation
    }
    
    // Getter and Setter
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        this.age = age;
    }
    
    // Instance method
    public String introduce() {
        return "Hi, I'm " + name + " and I'm " + age + " years old";
    }
    
    // Static method
    public static boolean isAdult(int age) {
        return age >= 18;
    }
    
    // toString method
    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
    
    // equals and hashCode
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return age == person.age && Objects.equals(name, person.name);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}

// Inheritance
public class Student extends Person {
    private String school;
    
    public Student(String name, int age, String school) {
        super(name, age);
        this.school = school;
    }
    
    public String getSchool() {
        return school;
    }
    
    public void setSchool(String school) {
        this.school = school;
    }
    
    public String study() {
        return getName() + " is studying at " + school;
    }
    
    // Method overriding
    @Override
    public String introduce() {
        return "Hi, I'm " + getName() + ", I'm " + getAge() + " and I study at " + school;
    }
}

// Interface for multiple inheritance-like behavior
interface Employee {
    int getSalary();
    void setSalary(int salary);
    default String work() {
        return "Working...";
    }
}

// Class implementing interface
public class WorkingStudent extends Student implements Employee {
    private int salary;
    
    public WorkingStudent(String name, int age, String school, int salary) {
        super(name, age, school);
        this.salary = salary;
    }
    
    @Override
    public int getSalary() {
        return salary;
    }
    
    @Override
    public void setSalary(int salary) {
        this.salary = salary;
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 25);
        Student student = new Student("Bob", 20, "MIT");
        WorkingStudent worker = new WorkingStudent("Charlie", 22, "Harvard", 50000);
        
        System.out.println(person.introduce());
        System.out.println(student.study());
        System.out.println(worker.work());
    }
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
    items = [1, 2, 3]
    print(items[num])
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except IndexError:
    print("Index out of range!")
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
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Custom exceptions
class CustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

try:
    raise CustomError("Something went wrong", 500)
except CustomError as e:
    print(f"Error {e.error_code}: {e}")

# Context managers
class ResourceManager:
    def __enter__(self):
        print("Acquiring resource")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False

with ResourceManager() as resource:
    print("Using resource")
```

### Java
```java
import java.io.*;
import java.util.*;

public class ExceptionHandling {
    
    // Basic try-catch
    public static void basicException() {
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        }
    }
    
    // Multiple catch blocks
    public static void multipleExceptions() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter a number: ");
            int num = scanner.nextInt();
            int result = 10 / num;
            int[] items = {1, 2, 3};
            System.out.println(items[num]);
        } catch (InputMismatchException e) {
            System.out.println("Invalid input!");
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero!");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index out of range!");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            System.out.println("Cleanup code here");
            scanner.close();
        }
    }
    
    // Multi-catch (Java 7+)
    public static void multiCatch() {
        try {
            // Some risky operation
        } catch (IOException | SQLException e) {
            System.out.println("IO or SQL error: " + e.getMessage());
        }
    }
    
    // Throwing exceptions
    public static int validateAge(int age) throws IllegalArgumentException {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        if (age > 150) {
            throw new IllegalArgumentException("Age seems unrealistic");
        }
        return age;
    }
    
    // Custom exceptions
    public static class CustomException extends Exception {
        private final int errorCode;
        
        public CustomException(String message, int errorCode) {
            super(message);
            this.errorCode = errorCode;
        }
        
        public int getErrorCode() {
            return errorCode;
        }
    }
    
    public static void throwCustomException() throws CustomException {
        throw new CustomException("Something went wrong", 500);
    }
    
    // Try-with-resources (Java 7+)
    public static void resourceManagement() {
        try (FileReader file = new FileReader("example.txt");
             BufferedReader reader = new BufferedReader(file)) {
            
            String line = reader.readLine();
            System.out.println(line);
            
        } catch (IOException e) {
            System.out.println("File error: " + e.getMessage());
        }
        // Resources are automatically closed
    }
    
    // Custom resource class
    public static class ResourceManager implements AutoCloseable {
        public ResourceManager() {
            System.out.println("Acquiring resource");
        }
        
        public void doSomething() {
            System.out.println("Using resource");
        }
        
        @Override
        public void close() {
            System.out.println("Releasing resource");
        }
    }
    
    public static void customResource() {
        try (ResourceManager resource = new ResourceManager()) {
            resource.doSomething();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        try {
            validateAge(25);
            throwCustomException();
        } catch (CustomException e) {
            System.out.println("Error " + e.getErrorCode() + ": " + e.getMessage());
        }
    }
}
```

---

## File Operations

### Python
```python
import os
import json

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

# Working with different encodings
with open("unicode.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 世界!")

# JSON operations
data = {"name": "John", "age": 30, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

# File operations
if os.path.exists("example.txt"):
    print("File exists")
    print("File size:", os.path.getsize("example.txt"))

os.rename("example.txt", "renamed.txt")
# os.remove("renamed.txt")  # Delete file

# Directory operations
os.makedirs("new_directory", exist_ok=True)
files = os.listdir(".")
for file in files:
    print(file)

# Exception handling with files
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
```

### Java
```java
import java.io.*;
import java.nio.file.*;
import java.util.*;
import com.fasterxml.jackson.databind.ObjectMapper;  // For JSON

public class FileOperations {
    
    // Writing to file
    public static void writeFile() throws IOException {
        try (FileWriter writer = new FileWriter("example.txt")) {
            writer.write("Hello, World!\n");
            writer.write("Java file operations");
        }
    }
    
    // Reading from file
    public static void readFile() throws IOException {
        try (FileReader reader = new FileReader("example.txt");
             BufferedReader bufferedReader = new BufferedReader(reader)) {
            
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
        }
    }
    
    // Reading entire file (Java 8+)
    public static void readFileModern() throws IOException {
        String content = Files.readString(Paths.get("example.txt"));
        System.out.println(content);
        
        // Reading all lines
        List<String> lines = Files.readAllLines(Paths.get("example.txt"));
        lines.forEach(System.out::println);
    }
    
    // Writing with modern API
    public static void writeFileModern() throws IOException {
        String content = "Hello, World!\nJava file operations";
        Files.writeString(Paths.get("example.txt"), content);
        
        // Appending
        Files.writeString(Paths.get("example.txt"), "\nAppended text", 
                         StandardOpenOption.APPEND);
    }
    
    // Working with different encodings
    public static void unicodeFile() throws IOException {
        String content = "Hello, 世界!";
        Files.writeString(Paths.get("unicode.txt"), content, 
                         StandardCharsets.UTF_8);
    }
    
    // JSON operations (requires Jackson library)
    public static class Person {
        public String name;
        public int age;
        public String city;
        
        // Constructors, getters, setters...
        public Person() {}
        public Person(String name, int age, String city) {
            this.name = name;
            this.age = age;
            this.city = city;
        }
    }
    
    public static void jsonOperations() throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        
        // Writing JSON
        Person person = new Person("John", 30, "New York");
        mapper.writeValue(new File("data.json"), person);
        
        // Reading JSON
        Person loaded = mapper.readValue(new File("data.json"), Person.class);
        System.out.println("Loaded: " + loaded.name);
    }
    
    // File operations
    public static void fileOperations() throws IOException {
        Path path = Paths.get("example.txt");
        
        if (Files.exists(path)) {
            System.out.println("File exists");
            System.out.println("File size: " + Files.size(path));
        }
        
        // Moving/renaming files
        Files.move(path, Paths.get("renamed.txt"), StandardCopyOption.REPLACE_EXISTING);
        
        // Deleting files
        // Files.delete(Paths.get("renamed.txt"));
        
        // Directory operations
        Files.createDirectories(Paths.get("new_directory"));
        
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(Paths.get("."))) {
            for (Path file : stream) {
                System.out.println(file.getFileName());
            }
        }
    }
    
    // Exception handling with files
    public static void fileExceptionHandling() {
        try {
            String content = Files.readString(Paths.get("nonexistent.txt"));
        } catch (NoSuchFileException e) {
            System.out.println("File not found!");
        } catch (AccessDeniedException e) {
            System.out.println("Permission denied!");
        } catch (IOException e) {
            System.out.println("IO Error: " + e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        try {
            writeFile();
            readFile();
            writeFileModern();
            readFileModern();
            fileOperations();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

## Collections and Data Structures

### Python
```python
# Lists (already covered above)
numbers = [1, 2, 3, 4, 5]

# Tuples (immutable)
coordinates = (10, 20)
person = ("John", 25, "Engineer")

# Tuple unpacking
x, y = coordinates
name, age, job = person

# Sets (unique elements)
unique_numbers = {1, 2, 3, 4, 5}
set_from_list = set([1, 2, 2, 3, 3, 4])

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2          # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2   # {3, 4}
difference = set1 - set2     # {1, 2}

# Dictionaries (key-value pairs)
person_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Dictionary operations
person_dict["job"] = "Engineer"  # Add/update
age = person_dict.get("age", 0)  # Get with default
keys = person_dict.keys()
values = person_dict.values()
items = person_dict.items()

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}

# Advanced collections
from collections import defaultdict, Counter, deque

# DefaultDict
dd = defaultdict(list)
dd["fruits"].append("apple")

# Counter
text = "hello world"
counter = Counter(text)  # Count character frequency

# Deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to front
dq.append(4)      # Add to back
left = dq.popleft()  # Remove from front
right = dq.pop()     # Remove from back
```

### Java
```java
import java.util.*;
import java.util.stream.Collectors;

public class Collections {
    
    public static void demonstrateCollections() {
        // ArrayList (dynamic array)
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        
        // LinkedList (doubly-linked list)
        LinkedList<String> linkedList = new LinkedList<>();
        linkedList.addFirst("first");
        linkedList.addLast("last");
        
        // HashSet (unique elements, unordered)
        Set<Integer> uniqueNumbers = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> setFromArray = new HashSet<>(Arrays.asList(1, 2, 2, 3, 3, 4));
        
        // TreeSet (sorted unique elements)
        Set<Integer> sortedSet = new TreeSet<>(Arrays.asList(5, 1, 3, 2, 4));
        
        // Set operations
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(3, 4, 5, 6));
        
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);  // {1, 2, 3, 4, 5, 6}
        
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);  // {3, 4}
        
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);  // {1, 2}
        
        // HashMap (key-value pairs)
        Map<String, Object> personMap = new HashMap<>();
        personMap.put("name", "John");
        personMap.put("age", 25);
        personMap.put("city", "New York");
        
        // Map operations
        personMap.put("job", "Engineer");  // Add/update
        int age = (Integer) personMap.getOrDefault("age", 0);  // Get with default
        Set<String> keys = personMap.keySet();
        Collection<Object> values = personMap.values();
        Set<Map.Entry<String, Object>> entries = personMap.entrySet();
        
        // TreeMap (sorted keys)
        Map<String, Integer> sortedMap = new TreeMap<>();
        
        // LinkedHashMap (maintains insertion order)
        Map<String, Integer> orderedMap = new LinkedHashMap<>();
        
        // Stream operations for map-like transformations
        Map<Integer, Integer> squaresMap = numbers.stream()
            .collect(Collectors.toMap(x -> x, x -> x * x));
        
        // Queue implementations
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);  // Add to back
        queue.offer(2);
        int front = queue.poll();  // Remove from front
        
        // Deque (double-ended queue)
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addFirst(0);   // Add to front
        deque.addLast(4);    // Add to back
        int left = deque.removeFirst();   // Remove from front
        int right = deque.removeLast();   // Remove from back
        
        // Priority Queue (heap)
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Stack
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        int top = stack.pop();
        
        // Properties (like dictionary)
        Properties props = new Properties();
        props.setProperty("name", "John");
        props.setProperty("age", "25");
    }
    
    // Custom comparable class
    public static class Person implements Comparable<Person> {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public int compareTo(Person other) {
            return Integer.compare(this.age, other.age);
        }
        
        // getters, setters, toString, equals, hashCode...
    }
    
    public static void main(String[] args) {
        demonstrateCollections();
        
        // Using custom comparable
        List<Person> people = Arrays.asList(
            new Person("Alice", 30),
            new Person("Bob", 25),
            new Person("Charlie", 35)
        );
        
        Collections.sort(people);  // Sorts by age
        
        // Custom comparator
        people.sort(Comparator.comparing(p -> p.name));  // Sort by name
    }
}
```

---

## Key Differences Summary

| Feature | Python | Java |
|---------|--------|------|
| **Typing** | Dynamic | Static |
| **Compilation** | Interpreted | Compiled to bytecode |
| **Syntax** | Indentation-based | Brace-based |
| **Memory Management** | Automatic (GC) | Automatic (GC) |
| **Performance** | Slower | Faster |
| **Platform** | Cross-platform | Cross-platform (JVM) |
| **Learning Curve** | Easier | Moderate |
| **Verbosity** | Concise | More verbose |
| **Object-Oriented** | Multi-paradigm | Primarily OOP |
| **Functional Programming** | Some support | Strong support (Java 8+) |
| **Package Management** | pip | Maven/Gradle |
| **IDE Support** | Good | Excellent |
| **Enterprise Use** | Growing | Dominant |
| **Data Science** | Dominant | Limited |
| **Web Development** | Django/Flask | Spring/Spring Boot |
| **Mobile Development** | Limited | Android native |

---

## Use Cases Comparison

### Python Best For:
- Data Science and Machine Learning
- Rapid prototyping
- Scripting and automation
- Web development (Django, Flask)
- Scientific computing
- AI and deep learning

### Java Best For:
- Enterprise applications
- Android development
- Large-scale systems
- Backend services
- Desktop applications (Swing, JavaFX)
- Microservices architecture

---

*This comparison covers the most common syntax patterns and features. Both languages have extensive ecosystems with numerous frameworks and libraries available.*