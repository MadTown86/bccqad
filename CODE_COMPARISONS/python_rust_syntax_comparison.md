# Python vs Rust Syntax Comparison

A comprehensive side-by-side comparison of Python and Rust syntax with examples.

---

## Table of Contents
1. [Basic Program Structure](#basic-program-structure)
2. [Variables and Data Types](#variables-and-data-types)
3. [Input/Output](#inputoutput)
4. [Conditional Statements](#conditional-statements)
5. [Loops](#loops)
6. [Functions](#functions)
7. [Arrays/Lists/Vectors](#arrayslistsvectors)
8. [Structs and Classes](#structs-and-classes)
9. [Error Handling](#error-handling)
10. [File Operations](#file-operations)
11. [Collections and Data Structures](#collections-and-data-structures)
12. [Memory Management](#memory-management)

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

# Importing modules
import math
from datetime import datetime
```

### Rust
```rust
// Simple Hello World
fn main() {
    println!("Hello, World!");
}

// With separate function
fn hello() {
    println!("Hello, World!");
}

fn main() {
    hello();
}

// With constants and variables
const MAX_SIZE: u32 = 100;

fn main() {
    let x = 10;
    println!("Value of x: {}", x);
}

// Using external crates (in Cargo.toml)
use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
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

# Mutable vs immutable (lists vs tuples)
mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)
```

### Rust
```rust
fn main() {
    // Static typing with type inference
    let name = "John";              // &str (string slice)
    let age = 25;                   // i32 (default integer)
    let height = 5.9;               // f64 (default float)
    let is_student = true;          // bool
    let numbers = vec![1, 2, 3];    // Vec<i32>
    
    // Explicit type annotations
    let name: &str = "John";
    let age: i32 = 25;
    let height: f64 = 5.9;
    
    // Mutable vs immutable
    let x = 5;          // immutable by default
    let mut y = 5;      // mutable
    y = 10;             // OK
    // x = 10;          // Error! x is immutable
    
    // Constants (must be known at compile time)
    const PI: f64 = 3.14159;
    const MAX_SIZE: u32 = 100;
    
    // Option type (instead of null/None)
    let result: Option<i32> = None;
    let some_number: Option<i32> = Some(42);
    
    // Multiple assignment (destructuring)
    let (x, y, z) = (1, 2, 3);
    
    // Different integer types
    let small: i8 = 127;
    let big: i64 = 9223372036854775807;
    let unsigned: u32 = 4294967295;
    
    // String types
    let string_slice: &str = "Hello";           // String slice
    let owned_string: String = String::from("Hello");  // Owned string
    let mut mutable_string = String::new();
    mutable_string.push_str("Hello");
}
```

---

## Input/Output

### Python
```python
# Output
print("Hello")
print("Name:", name)
print(f"Age: {age}")  # f-string formatting
print("Sum: {}".format(x + y))

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

# File-like output
import sys
print("Error message", file=sys.stderr)
```

### Rust
```rust
use std::io;

fn main() {
    // Output
    println!("Hello");
    let name = "John";
    let age = 25;
    println!("Name: {}", name);
    println!("Age: {}", age);
    println!("Age: {age}");  // Rust 1.58+ formatting
    
    // Input
    println!("Enter name: ");
    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read line");
    let name = name.trim(); // Remove newline
    
    println!("Enter age: ");
    let mut age_input = String::new();
    io::stdin()
        .read_line(&mut age_input)
        .expect("Failed to read line");
    let age: i32 = age_input
        .trim()
        .parse()
        .expect("Invalid number");
    
    // Multiple values
    let (x, y, z) = (1, 2, 3);
    println!("Values: {} {} {}", x, y, z);
    println!("Sum: {}", x + y + z);
    
    // Different output methods
    print!("No newline");
    println!(" continues here");
    eprintln!("Error message");  // stderr
    
    // Debug printing
    let numbers = vec![1, 2, 3];
    println!("{:?}", numbers);   // Debug format
    println!("{:#?}", numbers);  // Pretty debug format
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

# Checking for None
if result is not None:
    print("Has result")
```

### Rust
```rust
fn main() {
    let age = 25;
    
    // If-else if-else
    if age < 18 {
        println!("Minor");
    } else if age < 65 {
        println!("Adult");
    } else {
        println!("Senior");
    }
    
    // If as expression (returns value)
    let status = if age >= 18 { "Adult" } else { "Minor" };
    
    // Multiple conditions
    if age >= 18 && age < 65 {
        println!("Working age");
    }
    
    // Pattern matching with match
    let grade = 'A';
    match grade {
        'A' => println!("Excellent"),
        'B' => println!("Good"),
        'C' => println!("Average"),
        _ => println!("Try harder"),
    }
    
    // Match with ranges
    let score = 85;
    match score {
        90..=100 => println!("A"),
        80..=89 => println!("B"),
        70..=79 => println!("C"),
        60..=69 => println!("D"),
        _ => println!("F"),
    }
    
    // Option matching
    let result: Option<i32> = Some(42);
    match result {
        Some(value) => println!("Got value: {}", value),
        None => println!("No value"),
    }
    
    // If let (pattern matching shorthand)
    if let Some(value) = result {
        println!("Got value: {}", value);
    }
    
    // Boolean evaluation
    let items = vec![1, 2, 3];
    if !items.is_empty() {
        println!("Has items");
    }
    
    // Checking for Some/None
    if result.is_some() {
        println!("Has result");
    }
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

# For-else
for i in range(5):
    if i == 10:  # This won't happen
        break
else:
    print("Loop completed normally")
```

### Rust
```rust
fn main() {
    // For loop with range
    for i in 0..5 {
        println!("{}", i);
    }
    
    // For loop with inclusive range
    for i in 0..=5 {
        println!("{}", i);
    }
    
    // For loop with vector
    let fruits = vec!["apple", "banana", "orange"];
    for fruit in &fruits {
        println!("{}", fruit);
    }
    
    // For loop with enumerate
    for (index, fruit) in fruits.iter().enumerate() {
        println!("{}: {}", index, fruit);
    }
    
    // While loop
    let mut count = 0;
    while count < 5 {
        println!("{}", count);
        count += 1;
    }
    
    // Loop (infinite loop with break)
    let mut x = 0;
    loop {
        if x >= 5 {
            break;
        }
        println!("{}", x);
        x += 1;
    }
    
    // Iterator methods (similar to comprehensions)
    let squares: Vec<i32> = (0..10).map(|x| x * x).collect();
    let evens: Vec<i32> = (0..20).filter(|&x| x % 2 == 0).collect();
    
    // Nested loops
    for i in 0..3 {
        for j in 0..3 {
            println!("({}, {})", i, j);
        }
    }
    
    // Loop control
    for i in 0..10 {
        if i == 3 {
            continue;
        }
        if i == 7 {
            break;
        }
        println!("{}", i);
    }
    
    // Loop with labels (for nested loops)
    'outer: for i in 0..3 {
        for j in 0..3 {
            if i == 1 && j == 1 {
                break 'outer;
            }
            println!("({}, {})", i, j);
        }
    }
    
    // Loop as expression (returns value)
    let result = loop {
        count += 1;
        if count == 10 {
            break count * 2;
        }
    };
    println!("Result: {}", result);
}
```

---

## Functions

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

# Generator function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Type hints
def add_numbers(a: int, b: int) -> int:
    return a + b

# Call examples
message = greet("Alice")
name, age = get_name_age()
result = square(5)
flexible_function(1, 2, 3, name="John", age=25)
sum_result = apply_operation(3, 4, add)
```

### Rust
```rust
// Basic function
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

// Function with default-like behavior using Option
fn greet_with_title(name: &str, title: Option<&str>) -> String {
    let title = title.unwrap_or("Mr.");
    format!("Hello, {} {}!", title, name)
}

// Function returning multiple values using tuple
fn get_name_age() -> (&'static str, i32) {
    ("John", 25)
}

// Function with references
fn modify_value(x: &mut i32) {
    *x += 1;
}

// Generic function
fn print_value<T: std::fmt::Display>(value: T) {
    println!("Value: {}", value);
}

// Function with closures
fn apply_operation<F>(x: i32, y: i32, operation: F) -> i32
where
    F: Fn(i32, i32) -> i32,
{
    operation(x, y)
}

// Higher-order function
fn create_adder(x: i32) -> impl Fn(i32) -> i32 {
    move |y| x + y
}

// Function with Result return type
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

// Function with lifetimes
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

// Iterator (similar to generator)
fn fibonacci() -> impl Iterator<Item = u64> {
    let mut a = 0;
    let mut b = 1;
    std::iter::from_fn(move || {
        let result = a;
        let next = a + b;
        a = b;
        b = next;
        Some(result)
    })
}

fn main() {
    // Function calls
    let message = greet("Alice");
    let (name, age) = get_name_age();
    
    // Closures
    let square = |x| x * x;
    let add = |x, y| x + y;
    
    let result = square(5);
    let sum_result = apply_operation(3, 4, add);
    
    // Using the adder
    let add_five = create_adder(5);
    let result = add_five(10); // 15
    
    // Error handling
    match divide(10.0, 2.0) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
    
    // Using the fibonacci iterator
    for num in fibonacci().take(10) {
        println!("{}", num);
    }
    
    // Mutable reference
    let mut x = 5;
    modify_value(&mut x);
    println!("x is now: {}", x);
    
    // Generic function
    print_value(42);
    print_value("Hello");
}
```

---

## Arrays/Lists/Vectors

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

# Array module for typed arrays
import array
int_array = array.array('i', [1, 2, 3, 4, 5])

# NumPy arrays (external library)
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
```

### Rust
```rust
use std::collections::VecDeque;

fn main() {
    // Arrays (fixed size, stack allocated)
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    let zeros = [0; 10];  // Array of 10 zeros
    
    // Vectors (dynamic, heap allocated)
    let mut vec_numbers = vec![1, 2, 3, 4, 5];
    let mut empty_vec: Vec<i32> = Vec::new();
    
    // Vector operations
    vec_numbers.push(6);                    // Add element
    vec_numbers.insert(0, 0);               // Insert at index
    let index = vec_numbers.iter().position(|&x| x == 3).unwrap();
    vec_numbers.remove(index);              // Remove at index
    let popped = vec_numbers.pop();         // Remove and return last (Option)
    let length = vec_numbers.len();         // Get length
    
    // Slicing (returns slice &[T])
    let first_three = &vec_numbers[..3];
    let last_two = &vec_numbers[vec_numbers.len()-2..];
    
    // Vector methods
    let mut more_numbers = vec![7, 8, 9];
    vec_numbers.append(&mut more_numbers);  // Add multiple elements
    vec_numbers.sort();                     // Sort in place
    let mut sorted_copy = vec_numbers.clone();
    sorted_copy.sort();
    vec_numbers.reverse();                  // Reverse in place
    
    // Iterator methods (similar to comprehensions)
    let squares: Vec<i32> = (1..6).map(|x| x * x).collect();
    let evens: Vec<i32> = vec_numbers.iter()
        .filter(|&&x| x % 2 == 0)
        .copied()
        .collect();
    
    // Nested vectors
    let matrix = vec![
        vec![1, 2, 3],
        vec![4, 5, 6],
        vec![7, 8, 9],
    ];
    
    // Different collection types
    let mut deque: VecDeque<i32> = VecDeque::new();
    deque.push_back(1);
    deque.push_front(0);
    
    // Array/slice iteration
    for number in &numbers {
        println!("{}", number);
    }
    
    for (index, number) in vec_numbers.iter().enumerate() {
        println!("{}: {}", index, number);
    }
    
    // Capacity management
    let mut vec_with_capacity = Vec::with_capacity(10);
    println!("Capacity: {}", vec_with_capacity.capacity());
    
    // Converting between types
    let array_from_vec: [i32; 3] = [vec_numbers[0], vec_numbers[1], vec_numbers[2]];
    let vec_from_array = numbers.to_vec();
    let slice_from_vec = &vec_numbers[..];
    
    // Accessing elements safely
    match vec_numbers.get(10) {
        Some(value) => println!("Value at index 10: {}", value),
        None => println!("Index 10 is out of bounds"),
    }
}
```

---

## Structs and Classes

### Python
```python
# Basic class
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

# Dataclass (Python 3.7+)
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

# Usage
person = Person("Alice", 25)
student = Student("Bob", 20, "MIT")
point = Point(3.0, 4.0)
```

### Rust
```rust
// Basic struct
#[derive(Debug, Clone, PartialEq)]
struct Person {
    name: String,
    age: u32,
}

impl Person {
    // Associated function (similar to class method)
    fn new(name: String, age: u32) -> Person {
        Person { name, age }
    }
    
    // Method (takes &self)
    fn introduce(&self) -> String {
        format!("Hi, I'm {} and I'm {} years old", self.name, self.age)
    }
    
    // Mutable method (takes &mut self)
    fn have_birthday(&mut self) {
        self.age += 1;
    }
    
    // Consuming method (takes self)
    fn into_name(self) -> String {
        self.name
    }
    
    // Static method
    fn is_adult(age: u32) -> bool {
        age >= 18
    }
    
    // Getter
    fn get_age(&self) -> u32 {
        self.age
    }
    
    // Setter with validation
    fn set_age(&mut self, age: u32) -> Result<(), String> {
        if age > 150 {
            Err("Age seems unrealistic".to_string())
        } else {
            self.age = age;
            Ok(())
        }
    }
}

// Implementing Display trait (similar to __str__)
impl std::fmt::Display for Person {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Person {{ name: '{}', age: {} }}", self.name, self.age)
    }
}

// Tuple struct
struct Point(f64, f64);

impl Point {
    fn distance_from_origin(&self) -> f64 {
        (self.0.powi(2) + self.1.powi(2)).sqrt()
    }
}

// Unit struct (no fields)
struct Empty;

// Struct with lifetimes
struct PersonRef<'a> {
    name: &'a str,
    age: u32,
}

// Enum (similar to inheritance for data)
#[derive(Debug)]
enum Shape {
    Circle { radius: f64 },
    Rectangle { width: f64, height: f64 },
    Square { side: f64 },
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle { radius } => std::f64::consts::PI * radius * radius,
            Shape::Rectangle { width, height } => width * height,
            Shape::Square { side } => side * side,
        }
    }
}

// Trait (similar to interface/abstract base class)
trait Drawable {
    fn draw(&self);
    
    // Default implementation
    fn description(&self) -> String {
        "A drawable object".to_string()
    }
}

impl Drawable for Shape {
    fn draw(&self) {
        match self {
            Shape::Circle { radius } => println!("Drawing circle with radius {}", radius),
            Shape::Rectangle { width, height } => {
                println!("Drawing rectangle {}x{}", width, height)
            }
            Shape::Square { side } => println!("Drawing square with side {}", side),
        }
    }
}

// Generic struct
#[derive(Debug)]
struct Container<T> {
    value: T,
}

impl<T> Container<T> {
    fn new(value: T) -> Self {
        Container { value }
    }
    
    fn get(&self) -> &T {
        &self.value
    }
    
    fn set(&mut self, value: T) {
        self.value = value;
    }
}

fn main() {
    // Creating instances
    let mut person = Person::new("Alice".to_string(), 25);
    println!("{}", person.introduce());
    
    person.have_birthday();
    println!("After birthday: {}", person);
    
    // Tuple struct
    let point = Point(3.0, 4.0);
    println!("Distance: {}", point.distance_from_origin());
    
    // Enum
    let circle = Shape::Circle { radius: 5.0 };
    let rectangle = Shape::Rectangle { width: 4.0, height: 6.0 };
    
    println!("Circle area: {}", circle.area());
    circle.draw();
    
    // Generic struct
    let int_container = Container::new(42);
    let string_container = Container::new("Hello".to_string());
    
    println!("Int container: {:?}", int_container);
    println!("String container: {:?}", string_container);
    
    // Pattern matching with structs
    match person {
        Person { name, age } if age >= 18 => {
            println!("{} is an adult", name);
        }
        Person { name, .. } => {
            println!("{} is a minor", name);
        }
    }
}
```

---

## Error Handling

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

# Context managers for cleanup
class ResourceManager:
    def __enter__(self):
        print("Acquiring resource")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False

with ResourceManager() as resource:
    print("Using resource")
    # Resource is automatically cleaned up
```

### Rust
```rust
use std::fs::File;
use std::io::{self, Read};

// Result type for error handling
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

// Using ? operator for error propagation
fn read_file_content(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content)
}

// Custom error types
#[derive(Debug)]
enum MathError {
    DivisionByZero,
    NegativeSquareRoot,
    InvalidInput(String),
}

impl std::fmt::Display for MathError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            MathError::DivisionByZero => write!(f, "Division by zero"),
            MathError::NegativeSquareRoot => write!(f, "Cannot take square root of negative number"),
            MathError::InvalidInput(msg) => write!(f, "Invalid input: {}", msg),
        }
    }
}

impl std::error::Error for MathError {}

fn safe_divide(a: f64, b: f64) -> Result<f64, MathError> {
    if b == 0.0 {
        Err(MathError::DivisionByZero)
    } else {
        Ok(a / b)
    }
}

fn safe_sqrt(x: f64) -> Result<f64, MathError> {
    if x < 0.0 {
        Err(MathError::NegativeSquareRoot)
    } else {
        Ok(x.sqrt())
    }
}

// Option type for values that might not exist
fn find_item(items: &[i32], target: i32) -> Option<usize> {
    items.iter().position(|&x| x == target)
}

// panic! for unrecoverable errors
fn validate_age(age: i32) -> i32 {
    if age < 0 {
        panic!("Age cannot be negative: {}", age);
    }
    age
}

// Using unwrap, expect, and proper error handling
fn demonstrate_error_handling() {
    // Result handling
    match divide(10.0, 2.0) {
        Ok(result) => println!("Result: {}", result),
        Err(error) => println!("Error: {}", error),
    }
    
    // Using ? operator
    let content = match read_file_content("example.txt") {
        Ok(content) => content,
        Err(error) => {
            println!("Failed to read file: {}", error);
            return;
        }
    };
    
    // Option handling
    let items = vec![1, 2, 3, 4, 5];
    match find_item(&items, 3) {
        Some(index) => println!("Found at index: {}", index),
        None => println!("Item not found"),
    }
    
    // Using unwrap_or and unwrap_or_else
    let result = find_item(&items, 10).unwrap_or(0);
    let result2 = find_item(&items, 10).unwrap_or_else(|| {
        println!("Item not found, using default");
        0
    });
    
    // Chaining operations
    let result: Option<f64> = Some(16.0)
        .and_then(|x| safe_sqrt(x).ok())
        .map(|x| x * 2.0);
    
    // Converting between Option and Result
    let option_value: Option<i32> = Some(42);
    let result_value: Result<i32, &str> = option_value.ok_or("No value");
}

fn main() {
    demonstrate_error_handling();
    
    // Custom error handling
    match safe_divide(10.0, 0.0) {
        Ok(result) => println!("Result: {}", result),
        Err(MathError::DivisionByZero) => println!("Cannot divide by zero!"),
        Err(error) => println!("Math error: {}", error),
    }
}
```

---

## File Operations

### Python
```python
import os
import json
from pathlib import Path

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

# Using pathlib (modern approach)
path = Path("example.txt")
if path.exists():
    content = path.read_text()
    print(f"File size: {path.stat().st_size}")

# Directory operations
os.makedirs("new_directory", exist_ok=True)
files = os.listdir(".")
for file in files:
    print(file)

# Path operations with pathlib
current_dir = Path(".")
for file_path in current_dir.glob("*.txt"):
    print(file_path.name)

# Exception handling with files
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
```

### Rust
```rust
use std::fs::{self, File, OpenOptions};
use std::io::{self, Read, Write, BufRead, BufReader, BufWriter};
use std::path::Path;
use serde::{Serialize, Deserialize};
use serde_json;

// JSON serialization (requires serde crate)
#[derive(Serialize, Deserialize, Debug)]
struct Person {
    name: String,
    age: u32,
    city: String,
}

fn file_operations() -> io::Result<()> {
    // Writing to file
    let mut file = File::create("example.txt")?;
    file.write_all(b"Hello, World!\n")?;
    file.write_all(b"Rust file operations")?;
    
    // Alternative: write entire string at once
    fs::write("example2.txt", "Hello, World!\nRust file operations")?;
    
    // Reading from file
    let mut file = File::open("example.txt")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    println!("{}", content);
    
    // Alternative: read entire file at once
    let content = fs::read_to_string("example.txt")?;
    println!("{}", content);
    
    // Reading line by line
    let file = File::open("example.txt")?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        println!("{}", line?);
    }
    
    // Appending to file
    let mut file = OpenOptions::new()
        .append(true)
        .open("example.txt")?;
    file.write_all(b"\nAppended text")?;
    
    // Buffered writing for performance
    let file = File::create("buffered.txt")?;
    let mut writer = BufWriter::new(file);
    writer.write_all(b"Buffered writing")?;
    writer.flush()?; // Ensure data is written
    
    Ok(())
}

fn json_operations() -> Result<(), Box<dyn std::error::Error>> {
    // JSON serialization
    let person = Person {
        name: "John".to_string(),
        age: 30,
        city: "New York".to_string(),
    };
    
    let json_string = serde_json::to_string_pretty(&person)?;
    fs::write("data.json", json_string)?;
    
    // JSON deserialization
    let json_content = fs::read_to_string("data.json")?;
    let loaded_person: Person = serde_json::from_str(&json_content)?;
    println!("Loaded: {:?}", loaded_person);
    
    Ok(())
}

fn path_operations() -> io::Result<()> {
    // Path operations
    let path = Path::new("example.txt");
    
    if path.exists() {
        println!("File exists");
        let metadata = fs::metadata(path)?;
        println!("File size: {}", metadata.len());
        println!("Is file: {}", metadata.is_file());
        println!("Is directory: {}", metadata.is_dir());
    }
    
    // Directory operations
    fs::create_dir_all("new_directory")?;
    
    // List directory contents
    for entry in fs::read_dir(".")? {
        let entry = entry?;
        let path = entry.path();
        if path.is_file() {
            println!("File: {}", path.display());
        } else if path.is_dir() {
            println!("Directory: {}", path.display());
        }
    }
    
    // Copy and move files
    fs::copy("example.txt", "example_copy.txt")?;
    fs::rename("example_copy.txt", "example_renamed.txt")?;
    
    // Remove files and directories
    // fs::remove_file("example_renamed.txt")?;
    // fs::remove_dir_all("new_directory")?;
    
    Ok(())
}

fn error_handling_example() {
    match fs::read_to_string("nonexistent.txt") {
        Ok(content) => println!("File content: {}", content),
        Err(error) => match error.kind() {
            io::ErrorKind::NotFound => println!("File not found!"),
            io::ErrorKind::PermissionDenied => println!("Permission denied!"),
            _ => println!("Other error: {}", error),
        },
    }
}

fn main() {
    if let Err(error) = file_operations() {
        println!("File operation error: {}", error);
    }
    
    if let Err(error) = json_operations() {
        println!("JSON operation error: {}", error);
    }
    
    if let Err(error) = path_operations() {
        println!("Path operation error: {}", error);
    }
    
    error_handling_example();
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

# Sets (unique elements)
unique_numbers = {1, 2, 3, 4, 5}
set_from_list = set([1, 2, 2, 3, 3, 4])

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2          # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2   # {3, 4}
difference = set1 - set2     # {1, 2}

# Dictionaries (hash maps)
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

# Advanced collections
from collections import defaultdict, Counter, deque, OrderedDict

# DefaultDict
dd = defaultdict(list)
dd["fruits"].append("apple")

# Counter (frequency counting)
text = "hello world"
counter = Counter(text)

# Deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to front
dq.append(4)      # Add to back

# OrderedDict (maintains insertion order)
od = OrderedDict([("a", 1), ("b", 2)])

# Named tuples
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
```

### Rust
```rust
use std::collections::{HashMap, HashSet, BTreeMap, BTreeSet, VecDeque, LinkedList};
use std::collections::hash_map::Entry;

fn demonstrate_collections() {
    // Vectors (already covered above)
    let mut numbers = vec![1, 2, 3, 4, 5];
    
    // Arrays and slices
    let array: [i32; 5] = [1, 2, 3, 4, 5];
    let slice = &array[1..4];
    
    // Tuples
    let coordinates = (10, 20);
    let person = ("John", 25, "Engineer");
    let (name, age, job) = person; // Destructuring
    
    // HashSet (unique elements)
    let mut unique_numbers = HashSet::new();
    unique_numbers.insert(1);
    unique_numbers.insert(2);
    unique_numbers.insert(3);
    
    // Set from iterator
    let set_from_vec: HashSet<i32> = numbers.iter().cloned().collect();
    
    // Set operations
    let set1: HashSet<i32> = [1, 2, 3, 4].iter().cloned().collect();
    let set2: HashSet<i32> = [3, 4, 5, 6].iter().cloned().collect();
    
    let union: HashSet<i32> = set1.union(&set2).cloned().collect();
    let intersection: HashSet<i32> = set1.intersection(&set2).cloned().collect();
    let difference: HashSet<i32> = set1.difference(&set2).cloned().collect();
    
    // HashMap (key-value pairs)
    let mut person_map = HashMap::new();
    person_map.insert("name", "John");
    person_map.insert("age", "25");
    person_map.insert("city", "New York");
    
    // HashMap operations
    person_map.insert("job", "Engineer");  // Add/update
    let age = person_map.get("age").unwrap_or(&"0");  // Get with default
    
    // Entry API for advanced operations
    let counter = person_map.entry("visits").or_insert("0");
    
    // Iterate over HashMap
    for (key, value) in &person_map {
        println!("{}: {}", key, value);
    }
    
    // BTreeMap (sorted keys)
    let mut sorted_map = BTreeMap::new();
    sorted_map.insert("c", 3);
    sorted_map.insert("a", 1);
    sorted_map.insert("b", 2);
    // Iteration is in sorted order
    
    // VecDeque (double-ended queue)
    let mut deque = VecDeque::new();
    deque.push_back(1);
    deque.push_back(2);
    deque.push_front(0);
    let front = deque.pop_front(); // Some(0)
    let back = deque.pop_back();   // Some(2)
    
    // LinkedList (doubly-linked list)
    let mut list = LinkedList::new();
    list.push_back(1);
    list.push_back(2);
    list.push_front(0);
    
    // Custom structs as collections
    #[derive(Debug)]
    struct Point {
        x: i32,
        y: i32,
    }
    
    let points = vec![
        Point { x: 1, y: 2 },
        Point { x: 3, y: 4 },
    ];
    
    // Frequency counting (like Counter)
    let text = "hello world";
    let mut char_count = HashMap::new();
    for ch in text.chars() {
        *char_count.entry(ch).or_insert(0) += 1;
    }
    
    println!("Character counts: {:?}", char_count);
}

// Custom data structures
#[derive(Debug)]
struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Stack { items: Vec::new() }
    }
    
    fn push(&mut self, item: T) {
        self.items.push(item);
    }
    
    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }
    
    fn peek(&self) -> Option<&T> {
        self.items.last()
    }
    
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
}

fn main() {
    demonstrate_collections();
    
    // Using custom stack
    let mut stack = Stack::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    
    while let Some(item) = stack.pop() {
        println!("Popped: {}", item);
    }
}
```

---

## Memory Management

### Python
```python
# Automatic memory management with garbage collection
import gc
import sys

# Creating objects
numbers = [1, 2, 3, 4, 5]
text = "Hello, World!"
dictionary = {"key": "value"}

# Reference counting
a = [1, 2, 3]
b = a  # b now references the same list
print(sys.getrefcount(a))  # Reference count

# Weak references (to avoid circular references)
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = weakref.ref(self)  # Weak reference to parent
        self.children.append(child)

# Memory usage
import tracemalloc

tracemalloc.start()
# Your code here
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
tracemalloc.stop()

# Forcing garbage collection
gc.collect()

# Context managers for resource cleanup
class ResourceManager:
    def __enter__(self):
        print("Acquiring resource")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")

with ResourceManager() as resource:
    # Resource is automatically cleaned up
    pass

# Memory-efficient generators
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Only creates one number at a time
fib = fibonacci_generator()
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(num)
```

### Rust
```rust
// Manual memory management with ownership system

fn demonstrate_ownership() {
    // Stack allocation (automatic cleanup)
    let x = 5;              // x owns the value 5
    let y = x;              // x is copied (i32 implements Copy)
    println!("{}, {}", x, y); // Both x and y are valid
    
    // Heap allocation (ownership transfer)
    let s1 = String::from("hello");  // s1 owns the string
    let s2 = s1;                     // Ownership moves to s2
    // println!("{}", s1);           // Error! s1 no longer valid
    println!("{}", s2);              // s2 is valid
    
    // Cloning for deep copy
    let s3 = String::from("world");
    let s4 = s3.clone();             // Deep copy
    println!("{}, {}", s3, s4);      // Both are valid
}

fn demonstrate_borrowing() {
    let s = String::from("hello");
    
    // Immutable borrowing
    let len = calculate_length(&s);  // Borrow s
    println!("Length of '{}' is {}.", s, len); // s is still valid
    
    // Mutable borrowing
    let mut s = String::from("hello");
    change_string(&mut s);           // Mutable borrow
    println!("{}", s);
    
    // Multiple immutable borrows are allowed
    let r1 = &s;
    let r2 = &s;
    println!("{} and {}", r1, r2);
    
    // But not immutable and mutable at the same time
    // let r3 = &mut s; // Error if r1 and r2 are still in scope
}

fn calculate_length(s: &String) -> usize {
    s.len()
} // s goes out of scope, but doesn't drop the value (it's borrowed)

fn change_string(s: &mut String) {
    s.push_str(", world");
}

// Lifetimes
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

// Reference counting for shared ownership
use std::rc::Rc;
use std::cell::RefCell;

fn demonstrate_rc() {
    let shared_data = Rc::new(vec![1, 2, 3, 4, 5]);
    let reference1 = Rc::clone(&shared_data);
    let reference2 = Rc::clone(&shared_data);
    
    println!("Reference count: {}", Rc::strong_count(&shared_data));
    // Data is dropped when last Rc goes out of scope
}

// Interior mutability with RefCell
fn demonstrate_refcell() {
    let data = Rc::new(RefCell::new(vec![1, 2, 3]));
    let reference1 = Rc::clone(&data);
    let reference2 = Rc::clone(&data);
    
    // Mutate through shared reference
    reference1.borrow_mut().push(4);
    reference2.borrow_mut().push(5);
    
    println!("{:?}", data.borrow());
}

// Smart pointers
use std::boxed::Box;

fn demonstrate_box() {
    // Box for heap allocation
    let boxed_value = Box::new(5);
    println!("Boxed value: {}", boxed_value);
    
    // Recursive types require Box
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }
    
    use List::{Cons, Nil};
    
    let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
    println!("{:?}", list);
}

// RAII (Resource Acquisition Is Initialization)
struct FileWrapper {
    name: String,
}

impl FileWrapper {
    fn new(name: String) -> Self {
        println!("Opening file: {}", name);
        FileWrapper { name }
    }
}

impl Drop for FileWrapper {
    fn drop(&mut self) {
        println!("Closing file: {}", self.name);
        // Cleanup happens automatically when going out of scope
    }
}

// Memory-safe iterator (no garbage collection needed)
fn demonstrate_iterators() {
    let numbers = vec![1, 2, 3, 4, 5];
    
    // Iterator is lazy and memory-efficient
    let doubled: Vec<i32> = numbers
        .iter()
        .map(|x| x * 2)
        .filter(|&x| x > 4)
        .collect();
    
    println!("Doubled and filtered: {:?}", doubled);
    
    // Original vector is still owned and valid
    println!("Original: {:?}", numbers);
}

fn main() {
    demonstrate_ownership();
    demonstrate_borrowing();
    demonstrate_rc();
    demonstrate_refcell();
    demonstrate_box();
    demonstrate_iterators();
    
    {
        let _file = FileWrapper::new("example.txt".to_string());
        // File is automatically "closed" when _file goes out of scope
    }
    println!("File has been closed");
    
    // Demonstrating lifetimes
    let string1 = String::from("abcd");
    let string2 = "xyz";
    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}
```

---

## Key Differences Summary

| Feature | Python | Rust |
|---------|--------|------|
| **Memory Management** | Garbage Collection | Ownership System |
| **Performance** | Interpreted, slower | Compiled, very fast |
| **Type System** | Dynamic typing | Static typing with inference |
| **Safety** | Runtime errors | Compile-time safety |
| **Learning Curve** | Easy | Steep |
| **Concurrency** | GIL limitations | Fearless concurrency |
| **Error Handling** | Exceptions | Result/Option types |
| **Package Manager** | pip | Cargo |
| **Runtime** | Python interpreter | Native binary |
| **Memory Usage** | Higher overhead | Minimal overhead |
| **Development Speed** | Very fast | Moderate |
| **Null Safety** | Runtime errors | Option<T> type |
| **Mutability** | Mutable by default | Immutable by default |

---

## Use Cases Comparison

### Python Best For:
- Rapid prototyping and scripting
- Data science and machine learning
- Web development (Django, Flask)
- Scientific computing
- Automation and tooling
- AI and deep learning
- Quick one-off scripts

### Rust Best For:
- System programming
- Performance-critical applications
- Safe concurrent programming
- WebAssembly applications
- Blockchain and cryptocurrency
- Game engines
- Operating systems and drivers
- Network services
- Command-line tools

---

## Philosophy Comparison

### Python Philosophy:
- "There should be one obvious way to do it"
- Readability and simplicity first
- "Batteries included" standard library
- Duck typing and flexibility
- Rapid development

### Rust Philosophy:
- "Fast, reliable, productive—pick three"
- Zero-cost abstractions
- Memory safety without garbage collection
- Preventing bugs at compile time
- Empowering systems programming

---

*This comparison highlights the fundamental differences between Python's ease-of-use approach and Rust's safety-and-performance focus. Choose Python for rapid development and high-level applications, choose Rust for performance-critical and systems-level programming.*