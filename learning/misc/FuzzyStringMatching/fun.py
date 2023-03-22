import re

from fuzzywuzzy import fuzz
from tabulate import tabulate


def distinct_characters(names):
    unique_chars = set()

    for name in names:
        for char in name:
            unique_chars.add(char)

    # Sort characters alphabetically and then by Unicode code point
    print(sorted(unique_chars, key=lambda c: (c.isalnum(), c.isalpha(), c)))


# normalize name unibet
def normalize_name_u(name):
    # Remove "\xa0" character
    name = name.replace('\xa0', ' ')

    # Split name into first and last names using ", "
    last_name, first_name = name.split(', ')

    # Remove specific unwanted characters (e.g., digits and certain punctuation marks)
    last_name = re.sub(r'[\d!"#$%&()*+,-./:;<=>?@[\\\]^_`{|}~\|]', '', last_name)
    first_name = re.sub(r'[\d!"#$%&()*+,-./:;<=>?@[\\\]^_`{|}~\|]', '', first_name)

    # Combine first and last names
    normalized_name = f"{first_name} {last_name}"
    return normalized_name


# normalize name oddset
def normalize_name_o(name):
    # Remove "\xa0" character
    name = name.replace('\xa0', ' ')

    # Split name into words using a single space
    words = name.split(' ')

    # Remove specific unwanted characters (e.g., digits and certain punctuation marks)
    cleaned_words = [re.sub(r'[\d!"#$%&()*+,-./:;<=>?@[\\\]^_`{|}~]', '', word) for word in words]
    # Combine cleaned words back into a single string
    normalized_name = ' '.join(cleaned_words)
    return normalized_name


def is_match(name1, name2, threshold=85):
    name1_words = name1.split()
    name2_words = name2.split()

    for word1 in name1_words:
        for word2 in name2_words:
            if fuzz.ratio(word1, word2) >= threshold:
                return True

    return False


def compare_name_lists(unibet_names, oddset_names):
    results = []

    matched_oddset_names = set()

    for name1 in unibet_names:
        best_match = None
        best_score = 0

        for name2 in oddset_names:
            if is_match(name1, name2) and name2 not in matched_oddset_names:
                best_match = name2
                best_score = fuzz.ratio(name1, name2)
                break

        if best_match:
            matched_oddset_names.add(best_match)
        results.append((name1, best_score, best_match))

    # Sort results by fuzz.ratio score in descending order
    results.sort(key=lambda x: x[1], reverse=True)

    # Print the table
    headers = ["Name (Unibet)", "Fuzz Ratio", "Name (Oddset)"]
    print(tabulate(results, headers=headers))

