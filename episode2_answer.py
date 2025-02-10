def main():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    return int(x) + int(y)

def alternate_main():
    return int(input("Enter a number: ")) + int(input("Enter another number: "))

if __name__ == "__main__":
    print(main())

    # One thing you may have struggled with here is that you didn't print your 'main()' function so no result was output.
    # The other issue would be that you didn't convert the inputs into integers but kept them as strings.
    # The third issue could be that you looked a bit deeper into things yourself and put both inputs into the function definition.
    # --> This calls them twice, once upon function creation and once upon function call.  This is why I used the input() function inside the function.

