"""making_some_classes
"""
from dataclasses import dataclass


@dataclass()
class Greeting:
    text: str
    count: int = 1


def main():
    say_hi = Greeting('Hello World!')
    return say_hi.text, say_hi.count


if __name__ == "__main__":
    print(main())
