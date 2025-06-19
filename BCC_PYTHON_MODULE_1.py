# BCC - PYTHON MODULE 1 - RE Module
import re

"""
There are two main things we are going to cover:
1. Pattern matching string syntax
    - Email Addresses
    - Exact Matching Formulas
    - Telephone Numbers
    - Complex Patterns (like log entries with timestamps, levels, emails, and IP addresses)
    - Complex Capturing of Mathematical Formulas
    - Replacing Text in a String
2. Different re module methods to use for searching strings


1. Pattern Matching String Syntax
These are some examples and ARE WHAT IS REFERRED TO AS 'REGULAR EXPRESSIONS'
'(?<=abc)def'
r'(?<=-)\w+'

***NOTE***: Each character in the above strings means something different and limits the search to find patterns that match it.

2. Methods and Ways To Initiate A Search
1a. re.search -> This scans a string to find the first location where the regular expression
1b. re.match -> This checks for a match only at the beginning of the string.
1c. re.findall -> This returns a list of all non-overlapping matches of the pattern in the string.
"""

"""
List Of Regular Expression Characters and Their Meanings:
- . (dot) - Matches any character except a newline.
- ^ (caret) - Matches the start of a string.
- $ (dollar) - Matches the end of a string.
- * (asterisk) - Matches zero or more occurrences of the preceding element.
- + (plus) - Matches one or more occurrences of the preceding element.
- ? (question mark) - Matches zero or one occurrence of the preceding element.
- {n} - Matches exactly n occurrences of the preceding element.
- {n,} - Matches n or more occurrences of the preceding element.
- {n,m} - Matches between n and m occurrences of the preceding element.
- [] (square brackets) - Matches any single character within the brackets.
- [^] (caret inside square brackets) - Matches any single character not within the brackets.
- | (pipe) - Acts as a logical OR between expressions.
- () (parentheses) - Groups expressions together and captures the matched text.
- \ (backslash) - Escapes a special character, allowing it to be treated as a literal character.
- \d - Matches any digit (equivalent to [0-9]).
- \D - Matches any non-digit character (equivalent to [^0-9]).
- \w - Matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
- \W - Matches any non-alphanumeric character (equivalent to [^a-zA-Z0-9_]).
- \s - Matches any whitespace character (spaces, tabs, newlines).
- \S - Matches any non-whitespace character.
- \b - Matches a word boundary (position between a word character and a non-word character).
- \B - Matches a non-word boundary (position between two word characters or two non-word characters).
- (?P<name>...) - Named group, allows you to refer to the group by name.
- (?P=name) - Matches the text matched by a named group.
- (?=...) - Positive lookahead, asserts that what follows the current position matches the pattern.
- (?!...) - Negative lookahead, asserts that what follows the current position does not match the pattern.
- (?<=...) - Positive lookbehind, asserts that what precedes the current position matches the pattern.
- (?<!...) - Negative lookbehind, asserts that what precedes the current position does not match the pattern.
# matches the pattern.
- re.IGNORECASE - Flag to perform case-insensitive matching.
- re.MULTILINE - Flag to allow ^ and $ to match the start and end of each line in a multi-line string.
- re.DOTALL - Flag to allow . to match any character, including newlines.
- re.VERBOSE - Flag to allow whitespace and comments in the pattern for better readability.
# matches the pattern.

The Different Methods:
- re.search(pattern, string, flags=0) - Searches the string for the first location where the pattern matches.
- re.match(pattern, string, flags=0) - Checks if the pattern matches at the beginning of the string.
- re.fullmatch(pattern, string, flags=0) - Checks if the entire string matches the pattern.
- re.findall(pattern, string, flags=0) - Returns a list of all non-overlapping matches of the pattern in the string.
- re.finditer(pattern, string, flags=0) - Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
- re.sub(pattern, repl, string, count=0, flags=0) - Replaces occurrences of the pattern in the string with the replacement string (repl).
"""


"""
It is difficult to showcase each pattern character individually, so we will focus on more complex examples that combine
multiple characters and methods to demonstrate their usage effectively.
"""

# Example Usage of re Module Methods:
def main():
   
    print("\n")
    # Example string to search
    text = "Hello, my email is john.doe@example.com.  Don't forget his wife's email is jane.doe@example.com."
    text_formula = "The cannon ball trajectory was calculated using the formula: y = ax^2 + bx + c.  My name is John Doe, and I am 30 years old."
    text_telephone = "You can reach me at 123-456-7890 or at my office number (987) 654-3210."
    text_telephone2 = "My contact numbers are 123.456.7890 and 9876543210. Your number is (123) 456-7890, and my friend's number is 987-654-3210."
    combined_telephone = [text_telephone, text_telephone2]
    log_entries = [
    "2024-03-15 14:23:45 [ERROR] User john.doe@company.com failed login from IP 192.168.1.100",
    "2024-03-15T14:24:12 [WARN] user jane_smith@test.org timeout on IP: 10.0.0.50",
    "2024/03/15 14:25:33 [INFO] successful login for admin@site.net from 172.16.0.1",
    "Mar 15 2024 14:26:01 [ERROR] bob.jones@domain.co.uk authentication failure (IP=203.0.113.45)"
]

    # Example 1: Using re.search to find an email address
    email_pattern = r'[\w.%_+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_match = re.search(email_pattern, text)
    print(f"Email found: {email_match.group() if email_match else 'No match found'}")
    
    # Example 2: Using re.findall to find all email addresses in a string
    findall_emails = re.findall(email_pattern, text)
    print(f"All emails found: {findall_emails if findall_emails else 'No matches found'}")

    """
    Lets break down the email pattern:
    1. [] - Things enclosed in square brackets means 'any character in the brackets'
    2. a-zA-Z0-9._%+- - This means any lowercase letter, uppercase letter, digit, dot, underscore, percent sign, plus sign, or hyphen.
    3. @ - This matches the '@' character literally.
    4. [a-zA-Z0-9.-]+ - This matches one or more occurrences of lowercase letters, uppercase letters, digits, dot, or hyphen.
    5. \. - This matches the '.' character literally (the backslash is used to escape the dot) - otherwise it wouldn't be recognized as something to match.
    6. [a-zA-Z]{2,} - This matches two or more occurrences of lowercase or uppercase letters (the domain extension).
    """

    # Example 2: Using re.search to find the first mathematical formula in a string in a literal sense
    formula_pattern = r'y\s*=\s*ax\^2\s*\+\s*bx\s*\+\s*c'
    formula_match = re.search(formula_pattern, text_formula)
    print(f"Formula found: {formula_match.group() if formula_match else 'No match found'}")

    """
    Lets break down the formula pattern:
    1. y - This matches the character 'y' literally.
    2. \s* - This matches zero or more whitespace characters.
    3. = - This matches the '=' character literally.
    4. ax\^2 - This matches the term 'ax^2' literally.
    5. \+ - This matches the '+' character literally.
    6. bx - This matches the term 'bx' literally.
    7. \+ - This matches the '+' character literally.
    8. c - This matches the character 'c' literally.
    """

    #Example 3: Using re.search to find a telephone number
    telephone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    telephone_match = re.search(telephone_pattern, text_telephone)
    print(f"Telephone number found: {telephone_match.group() if telephone_match else 'No match found'}")

    """Lets break down the telephone pattern:
    1. \(? - This matches an optional opening parenthesis.
    2. \d{3} - This matches exactly three digits (the area code).
    3. \)? - This matches an optional closing parenthesis.
    4. [-.\s]? - This matches an optional hyphen, dot, or whitespace character.
    5. \d{3} - This matches exactly three digits (the first part of the phone number).
    6. [-.\s]? - This matches an optional hyphen, dot, or whitespace character.
    7. \d{4} - This matches exactly four digits (the last part of the phone number).
    """
    # Example 4: Using re.compile to find all telephone numbers in multiple strings
    telephone_pattern_compiled = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    findall_telephones = telephone_pattern_compiled.findall(text_telephone2)
    print(f"All telephone numbers found: {findall_telephones if findall_telephones else 'No matches found'}")

    for entry in combined_telephone:
        findall_telephones = telephone_pattern_compiled.findall(entry)
        print(f"All telephone numbers found in entry: {findall_telephones if findall_telephones else 'No matches found'}")
    

    # Complex pattern to extract: timestamp, level, email, IP address
    pattern = r'''
        (?P<timestamp>                    # Named group for timestamp
            \d{4}[-/]?\d{2}[-/]?\d{2}    # Date: YYYY-MM-DD or YYYY/MM/DD
            [\sT]?                        # Optional space or T separator
            \d{2}:\d{2}:\d{2}            # Time: HH:MM:SS
            |                             # OR
            \w{3}\s+\d{1,2}\s+\d{4}\s+   # Mar 15 2024 format
            \d{2}:\d{2}:\d{2}
        )
        .*?                               # Non-greedy match for anything
        \[(?P<level>\w+)\]               # Log level in brackets
        .*?                               # More non-greedy matching
        (?P<email>                        # Email pattern
            [a-zA-Z0-9._%+-]+@           # Username part
            [a-zA-Z0-9.-]+\.[a-zA-Z]{2,} # Domain part
        )
        .*?                               # More content
        (?P<ip>                           # IP address pattern
            \b(?:\d{1,3}\.){3}\d{1,3}\b  # Standard IP format
        )
        '''

    # Compile the pattern with VERBOSE flag for readability
    regex = re.compile(pattern, re.VERBOSE)

    # Extract information from each log entry
    for entry in log_entries:
        match = regex.search(entry)
        if match:
            print(f"Timestamp: {match.group('timestamp')}")
            print(f"Level: {match.group('level')}")
            print(f"Email: {match.group('email')}")
            print(f"IP: {match.group('ip')}")
            print("-" * 40)

    # Pattern to match formulas like 'y = ax^2 + bx + c'
    formula_pattern = r'''
        (?P<left_side>                    # Left side of equation
            [a-zA-Z]                      # Single variable (y, f, etc.)
            (?:\([^)]+\))?                # Optional function notation like f(x)
        )
        \s*=\s*                           # Equals sign with optional whitespace
        (?P<right_side>                   # Right side - the expression
            (?:                           # Start of term group
                [+-]?                     # Optional sign
                \s*                       # Optional whitespace
                (?:                       # Coefficient options:
                    \d*\.?\d*             # Numeric coefficient (optional)
                    |                     # OR
                    [a-zA-Z]              # Letter coefficient
                )?
                [a-zA-Z]                  # Variable letter
                (?:\^[+-]?\d+)?           # Optional exponent
                |                         # OR constant term
                [+-]?\s*\d+\.?\d*         # Just a number
            )
            (?:                           # Additional terms
                \s*[+-]\s*                # Plus or minus
                (?:
                    (?:\d*\.?\d*|[a-zA-Z])?  # Optional coefficient
                    [a-zA-Z]                 # Variable
                    (?:\^[+-]?\d+)?          # Optional exponent
                    |                        # OR
                    \d+\.?\d*                # Constant
                )
            )*                            # Zero or more additional terms
        )
    '''

    # Test formulas
    formulas = [
        "y = ax^2 + bx + c",
        "f(x) = 2x^3 - 5x + 7",
        "z = 3.14x^2 + 2.5x - 1",
        "y = x^2 + x + 1",
        "p = -4q^3 + 2q^2 - q + 8",
        "f(t) = at^-2 + bt^-1 + c",
        "y = x",
        "area = πr^2"
    ]

    # Compile and test
    regex = re.compile(formula_pattern, re.VERBOSE)

    for formula in formulas:
        match = regex.search(formula)
        if match:
            print(f"Formula: {formula}")
            print(f"  Left: {match.group('left_side')}")
            print(f"  Right: {match.group('right_side')}")
            print()

    replacement_text = "The weather was nice in Europe.  Europe is a lot of fun to visit.  I love the culture in Europe.  I wish I were European. Europe is a great place to visit."
    # Example 3: Using re.sub to replace occurrences of 'Europe' with 'EU'
    replacement_pattern = r'\bEurope\b'
    replacement_result = re.sub(replacement_pattern, 'EU', replacement_text)

    print(replacement_result)

if __name__ == "__main__":
    main()