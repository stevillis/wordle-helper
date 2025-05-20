from typing import List


def get_vocabulary(file_path: str = "./br-sem-acentos.txt") -> List[str]:
    """Load vocabulary from a file, one word per line."""
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        vocabulary = f.read().splitlines()

    return vocabulary


def get_five_letter_words() -> List[str]:
    """Filter the vocabulary to only five-letter words."""
    vocabulary = get_vocabulary()
    return [word.lower() for word in vocabulary if len(word) == 5]


def find_words(
    five_letter_words: List[str],
    word_pattern: List[str],
) -> List[str]:
    """
    Find candidate words matching the pattern.
    word_pattern: List of 5 strings, each string is either a letter or empty
    (""), representing known letters in each position.
    """
    candidates = []
    for word in five_letter_words:
        match = True
        for i, letter in enumerate(word_pattern):
            if letter and word[i] != letter.lower():
                match = False
                break

        if match:
            candidates.append(word)

    return candidates
