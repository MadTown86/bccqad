# Python vs JavaScript Syntax Comparison

## Variables and Data Types

### Variable Declaration
**Python**
```python
# Variables are declared by assignment
name = "Alice"
age = 25
pi = 3.14159
```

**JavaScript**
```javascript
// Modern variable declarations
const name = "Alice";      // Immutable
let age = 25;             // Mutable, block-scoped
var pi = 3.14159;         // Mutable, function-scoped (legacy)
```

### Basic Data Types
**Python**
```python
# String
text = "Hello World"
multiline = """This is a
multiline string"""

# Numbers
integer = 42
float_num = 3.14
complex_num = 3 + 4j

# Boolean
is_active = True
is_disabled = False

# None
empty_value = None
```

**JavaScript**
```javascript
// String
const text = "Hello World";
const multiline = `This is a
multiline string`;

// Numbers (all numbers are floating point)
const integer = 42;
const floatNum = 3.14;

// Boolean
const isActive = true;
const isDisabled = false;

// Undefined and null
let emptyValue = undefined;
let nullValue = null;
```

## Data Structures

### Arrays/Lists
**Python**
```python
# Lists
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("banana")
print(fruits[0])  # First element
print(fruits[-1]) # Last element
```

**JavaScript**
```javascript
// Arrays
const fruits = ["apple", "banana", "orange"];
fruits.push("grape");
fruits.splice(1, 0, "kiwi");
fruits.splice(fruits.indexOf("banana"), 1);
console.log(fruits[0]);                    // First element
console.log(fruits[fruits.length - 1]);    // Last element
```

### Objects/Dictionaries
**Python**
```python
# Dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
person["email"] = "alice@example.com"
print(person["name"])
print(person.get("phone", "Not found"))
```

**JavaScript**
```javascript
// Objects
const person = {
    name: "Alice",
    age: 25,
    city: "New York"
};
person.email = "alice@example.com";
console.log(person.name);
console.log(person.phone || "Not found");
```

## Functions

### Basic Functions
**Python**
```python
# Function definition
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function call
message = greet("Alice")
custom_message = greet("Bob", "Hi")
```

**JavaScript**
```javascript
// Function declaration
function greet(name, greeting = "Hello") {
    return `${greeting}, ${name}!`;
}

// Arrow function (ES6)
const greet = (name, greeting = "Hello") => {
    return `${greeting}, ${name}!`;
};

// Concise arrow function
const greet = (name, greeting = "Hello") => `${greeting}, ${name}!`;

// Function call
const message = greet("Alice");
const customMessage = greet("Bob", "Hi");
```

### Anonymous Functions
**Python**
```python
# Lambda functions
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))

# Using lambda inline
sorted_words = sorted(["apple", "pie", "banana"], key=lambda x: len(x))
```

**JavaScript**
```javascript
// Anonymous functions
const square = (x) => x ** 2;
const numbers = [1, 2, 3, 4, 5];
const squared = numbers.map(square);

// Using anonymous functions inline
const sortedWords = ["apple", "pie", "banana"].sort((a, b) => a.length - b.length);
```

## Control Flow

### Conditionals
**Python**
```python
# If statements
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary operator
status = "adult" if age >= 18 else "minor"
```

**JavaScript**
```javascript
// If statements
const age = 18;
if (age >= 18) {
    console.log("Adult");
} else if (age >= 13) {
    console.log("Teenager");
} else {
    console.log("Child");
}

// Ternary operator
const status = age >= 18 ? "adult" : "minor";
```

### Loops
**Python**
```python
# For loops
for i in range(5):
    print(i)

# For loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

**JavaScript**
```javascript
// For loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// For...of loop (ES6)
const fruits = ["apple", "banana", "orange"];
for (const fruit of fruits) {
    console.log(fruit);
}

// For loop with index
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});

// While loop
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
```

## Classes and Objects

### Class Definition
**Python**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._private_var = "private"
    
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# Usage
person = Person("Alice", 25)
print(person.greet())
```

**JavaScript**
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
        this._privateVar = "private";
    }
    
    greet() {
        return `Hi, I'm ${this.name}`;
    }
    
    static fromString(personStr) {
        const [name, age] = personStr.split('-');
        return new Person(name, parseInt(age));
    }
    
    static isAdult(age) {
        return age >= 18;
    }
}

// Usage
const person = new Person("Alice", 25);
console.log(person.greet());
```

## Error Handling

**Python**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")
finally:
    print("Cleanup code")
```

**JavaScript**
```javascript
try {
    const result = 10 / 0; // This won't throw an error in JS
    throw new Error("Custom error");
} catch (error) {
    console.log(`Error: ${error.message}`);
} finally {
    console.log("Cleanup code");
}
```

## Asynchronous Programming

### Python (async/await)
```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    try:
        data = await fetch_data("https://api.example.com/data")
        print(data)
    except Exception as e:
        print(f"Error: {e}")

# Run the async function
asyncio.run(main())
```

### JavaScript (Promises and async/await)
```javascript
// Using fetch API with async/await
async function fetchData(url) {
    try {
        const response = await fetch(url);
        const data = await response.text();
        return data;
    } catch (error) {
        throw new Error(`Failed to fetch: ${error.message}`);
    }
}

async function main() {
    try {
        const data = await fetchData("https://api.example.com/data");
        console.log(data);
    } catch (error) {
        console.log(`Error: ${error.message}`);
    }
}

main();
```

## Key Differences Summary

| Feature | Python | JavaScript |
|---------|--------|------------|
| **Syntax Style** | Indentation-based | Curly braces `{}` |
| **Variable Declaration** | Direct assignment | `const`, `let`, `var` |
| **String Interpolation** | f-strings: `f"Hello {name}"` | Template literals: `` `Hello ${name}` `` |
| **Array Indexing** | Supports negative indexing | No negative indexing |
| **Type System** | Dynamically typed | Dynamically typed |
| **Scope** | Function and global scope | Function, block, and global scope |
| **This/Self** | Explicit `self` parameter | Implicit `this` context |
| **Truthiness** | `None`, `False`, `0`, `""`, `[]`, `{}` are falsy | `undefined`, `null`, `false`, `0`, `""`, `NaN` are falsy |
| **Equality** | `==` (equality), `is` (identity) | `==` (loose), `===` (strict) |
| **Comments** | `#` for single line, `"""` for multi-line | `//` for single line, `/* */` for multi-line |