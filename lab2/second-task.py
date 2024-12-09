#!/usr/bin/python3
import sys

def validate_name(name: str) -> None:
    if not name[0].isupper():
        raise ValueError(f"The name '{name}' must start with an uppercase letter!")
    
    if not name.isalpha():
        raise ValueError(f"The name '{name}' contains invalid characters!")

def greet_user(name: str) -> None:
    print(f"Nice to meet you {name}!")

def main():
    is_interactive = sys.stdin.isatty()

    if is_interactive:
        while True:
            try:
                name = input("Hello! What's your name?")
                validate_name(name)
                greet_user(name)

            except ValueError as e:
                print(f"Error: {e}", file=sys.stderr)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
    else:
        for line in sys.stdin:
            name = line.strip()
            try:
                validate_name(name)
                greet_user(name)
            except ValueError as e:
                print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
