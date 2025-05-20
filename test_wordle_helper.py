from unittest.mock import mock_open, patch

from wordle_helper import find_words, get_five_letter_words, get_vocabulary


@patch("builtins.open", new_callable=mock_open, read_data="word1\nword2\nword3\n")
def test_get_vocabulary_returns_list_of_words(mock_file):
    """Test that get_vocabulary returns a list of words from the file."""
    result = get_vocabulary("dummy/path.txt")

    # Check the file was opened with correct parameters
    mock_file.assert_called_once_with(file="dummy/path.txt", mode="r", encoding="utf-8")

    # Check the result is as expected
    assert result == ["word1", "word2", "word3"]


@patch("wordle_helper.get_vocabulary")
def test_get_five_letter_words_filters_correctly(mock_get_vocabulary):
    """Test that get_five_letter_words filters words correctly."""
    # Setup the mock to return a list with words of different lengths
    mock_get_vocabulary.return_value = [
        "word",
        "hello",
        "computer",
        "test",
        "five5",
        "a",
        "",
    ]

    result = get_five_letter_words()

    # Check that only 5-letter words are returned
    assert result == ["hello", "five5"]

    # Check that get_vocabulary was called
    mock_get_vocabulary.assert_called_once()


@patch("wordle_helper.get_vocabulary")
def test_get_five_letter_words_with_empty_vocabulary(mock_get_vocabulary):
    """Test that get_five_letter_words handles empty vocabulary correctly."""
    mock_get_vocabulary.return_value = []

    result = get_five_letter_words()

    assert result == []


@patch("wordle_helper.get_vocabulary")
def test_get_five_letter_words_with_no_matches(mock_get_vocabulary):
    """Test that get_five_letter_words handles no matches correctly."""
    mock_get_vocabulary.return_value = ["word", "a", "longword", "123"]

    result = get_five_letter_words()

    assert result == []


def test_find_words_with_exact_match():
    """Test that find_words finds exact matches."""
    five_letter_words = ["hello", "world", "tests", "tents"]
    word_pattern = ["h", "e", "l", "l", "o"]

    result = find_words(five_letter_words, word_pattern)

    assert result == ["hello"]


def test_find_words_with_partial_match():
    """Test that find_words finds partial matches."""
    five_letter_words = ["hello", "world", "tests", "tents"]
    word_pattern = ["t", "e", "", "", "s"]

    result = find_words(five_letter_words, word_pattern)

    assert set(result) == {"tests", "tents"}


def test_find_words_with_empty_pattern():
    """Test that find_words handles empty patterns correctly."""
    five_letter_words = ["hello", "world", "tests"]
    word_pattern = ["", "", "", "", ""]

    result = find_words(five_letter_words, word_pattern)

    assert result == ["hello", "world", "tests"]


def test_find_words_with_no_matches():
    """Test that find_words handles no matches correctly."""
    five_letter_words = ["hello", "world", "tests"]
    word_pattern = ["z", "", "", "", ""]

    result = find_words(five_letter_words, word_pattern)

    assert result == []


def test_find_words_with_empty_word_list():
    """Test that find_words handles empty word lists correctly."""
    five_letter_words = []
    word_pattern = ["h", "e", "l", "l", "o"]

    result = find_words(five_letter_words, word_pattern)

    assert result == []


def test_find_words_case_sensitivity():
    """Test that find_words is case sensitive."""
    five_letter_words = ["hello", "HELLO", "Hello", "hElLo"]
    word_pattern = ["h", "e", "l", "l", "o"]

    result = find_words(five_letter_words, word_pattern)

    assert result == ["hello"]
