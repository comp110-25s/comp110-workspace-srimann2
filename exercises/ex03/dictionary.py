__author__ = "730572401"

# Function implementations
def invert(d: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the input dictionary."""
    inverted: dict[str, str] = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("Duplicate key found when inverting dictionary!")
        inverted[value] = key
    return inverted

def count(values: list[str]) -> dict[str, int]:
    """Count the occurrences of each string in the list."""
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def favorite_color(people: dict[str, str]) -> str:
    """Determine the most common favorite color from a dictionary of people and their favorite colors."""
    color_count: dict[str, int] = count(list(people.values()))
    return max(color_count, key=lambda color: color_count[color])

def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words into a dictionary where keys are word lengths and values are sets of words of that length."""
    bins: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
    return bins
