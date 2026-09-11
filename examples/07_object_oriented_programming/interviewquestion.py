"""Runnable OOP interview revision prompts."""

QUESTIONS = [
    "What is OOP and why is it useful?",
    "Explain encapsulation, inheritance, polymorphism and abstraction.",
    "What is the difference between a class and an object?",
    "When would composition be preferable to inheritance?",
    "What are instance, class and static methods?",
    "What problem do dataclasses solve?",
    "How do __repr__ and __eq__ affect an object?",
]


def main() -> None:
    for index, question in enumerate(QUESTIONS, start=1):
        print(f"Q{index}. {question}")


if __name__ == "__main__":
    main()
