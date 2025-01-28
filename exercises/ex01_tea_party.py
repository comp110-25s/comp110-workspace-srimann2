"""Planning a Cozy Tea Party!"""

__author__: str = "730572401"


def main_planner(guests: int) -> None:
    "The entrypoint of the tea party planner"
    print(f"\nA Cozy Tea Party for {guests} People!\n")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    "Defines function for tea bags"
    return people * 2


def treats(people: int) -> int:
    """Defines treat function"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Defining cost function"
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
