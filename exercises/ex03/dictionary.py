__author__ = "730572401"

# Function implementations
def invert(d: dict[str, str]) -> dict[str, str]:
    """This inverts the keys and values of the input dictionary."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("Duplicate key found when inverting dictionary!")
        inverted[value] = key
    return inverted

def count(values: list[str]) -> dict[str, int]:
    """This counts the occurrences of each string in the list."""
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def favorite_colors(people: dict[str, str]) -> str:
    """This determines the most common favorite color from a dictionary of people and their favorite colors."""
    color_count = count(list(people.values()))
    return max(color_count, key=color_count.get)

def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins words into a dictionary where keys are word lengths and values are sets of words with have that length."""
    bins = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
    return bins
