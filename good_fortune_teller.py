"""
Fortune Teller - Good Coding Practices Version

Fortunes types: Career, love, health, life, lucky numbers, and lucky colors.

Good Coding Practices:
    Single Responsibility: Each function has one job.
    Documentation of Code: Module includes a module docstring, function docstrings, and parameter / return descriptions.
    Clean code: Meaningful function and variable names with consistent formatting throughout.
    Separation of Concerns: Code separates data, user interaction, business logic, and program control.
"""

import random
from typing import List
# Cannot update to Python 3.9 due to Windows error. Correcting the error by importing List from typing.


# Data

FORTUNES = {
    "career": ["A promotion is on the horizon.",
               "Your hard work will be recognized soon.",
               "A new opportunity will appear before you."],
    "love": ["Romance is in the air and closer than you think.",
             "Love is on the horizon, reach for it.",
             "Open your heart and love will follow."],
    "health": ["Rest and recovery is what you seek.",
               "A fresh routine will bring a second wind.",
               "Listen to your body; It won't lead you astray."],
    "life": ["A journey will change your perspective.",
             "Say yes. See where it will take you.",
             "Take the road less traveled. It will lead you far."],
}

LUCKY_NUMBERS = list(range(1, 100))
LUCKY_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "silver", "gold", "pink"]



# Core Functions

def get_fortune(category: str) -> str:
    """
    Return a random fortune string for the given category.

    Args:
        category: One of the keys in FORTUNES.

    Returns:
        A random fortune string for the given category or an error message if the category is unknown.
    """
    if category not in FORTUNES:
        return f"Unknown category '{category}'. Choose from: {list(FORTUNES.keys())}"
    return random.choice(FORTUNES[category])



def get_lucky_numbers(count: int = 3) -> List[int]:
    """
    Return a sorted list of 3 unique lucky numbers (1-99).

    Args:
        count: How many lucky numbers to generate (default 3).

    Returns:
        A sorted list of unique integers.
    """
    return sorted(random.sample(LUCKY_NUMBERS, count))



def get_lucky_colors() -> str:
    """
    Return a single random lucky color.
    """
    return random.choice(LUCKY_COLORS)

def choose_fortune_category():
    """
    Prompt the user to pick a valid fortune category from the available options.

    Keeps asking until a valid choice is entered.

    Returns:
        The chosen category string.
    """
    categories = list(FORTUNES.keys())
    print("\nAvailable fortune categories:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    while True:
        choice = input("\nEnter a fortune category number or name: ").strip().lower()

        # Accepts the number or the name
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(categories):
                return categories[index]
        elif choice in categories:
            return choice

        print(f"Invalid choice. Please enter a number (1-{len(categories)}) or a category name.")



# Entry point

def main() -> None:
    """
    Run the interactive fortune-teller session.
    """
    print("Welcome to the Fortune Teller!")

    while True:
        category = choose_fortune_category()

        print("\nYour fortune:")
        print(get_fortune(category))
        print(f"\nYour lucky numbers are: {get_lucky_numbers(3)}")
        print(f"\nYour lucky colors are: {get_lucky_colors()}")

        again = input("\nWould you like another fortune? (y/n): ").strip().lower()

        if again not in ["y", "yes"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()