"""
Word Occurrences
Estimate: 40 minutes
Actual:   55 minutes
"""


def count_word_occurrences(text):
    word_counts = {}

    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the length of the longest word for formatting
    max_word_length = max(len(word) for word in word_counts.keys())

    # Sort the word counts alphabetically
    sorted_word_counts = sorted(word_counts.items())

    # Print the word occurrences aligned
    for word, count in sorted_word_counts:
        print(f"{word:>{max_word_length}} : {count}")


# Test the function
text = input("Enter a string: ")
count_word_occurrences(text)
