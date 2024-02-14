from collections import deque


UKRAINIAN_CHARSET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдежзиіїйклмнопрстуфхцчшщьюя"


def is_palindrome(d: deque):
    while True:
        try:
            if d.pop() != d.popleft():
                return False
        except IndexError:
            return True


def dequefy(s: str):
    return deque("".join([c for c in s if c in UKRAINIAN_CHARSET or c.isalpha()]).lower())


def main():
    print("Welcome to the English/Ukrainian Palindrome Checker. Enter phrase or press any key to exit.")
    while True:
        print("Enter phrase to check if it is a palindrome:")
        phrase = input()
        if not phrase:
            print("Have a nice day!")
            break
        print(f"Phrase {"is" if is_palindrome(
            dequefy(phrase)) else "is not"} a palindrome")


if __name__ == "__main__":
    main()
