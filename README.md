# Wordle Helper

Wordle Helper is a simple application to help players of [Wordle](https://wordle.com/) (English) and [Termo](https://termo.pt/) (Portuguese) find 5-letter words based on known letters in each position.

![App preview](app_preview.png)

Access the app on [Streamlit Cloud](https://wordle-assistant.streamlit.app/).

## Features
- User-friendly Streamlit interface
- Quick search for candidate words based on known letters
- Support for partial patterns (leave boxes blank for unknown positions)
- Multi-language support (English and Portuguese)

## How to Use
1. Select your preferred language in the sidebar
2. Type the known letters in the corresponding position boxes (leave blank if unknown)
3. Click **Search** to see candidate words
4. Use the suggestions to advance in your game!

### Example
If you know that the second letter is 'A', fill only the second box:

| L1  | L2  | L3  | L4  | L5  |
| --- | --- | --- | --- | --- |
|     | A   |     |     |     |

The app will show all 5-letter words with 'A' in the second position.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/stevillis/wordle-helper.git
   cd wordle-helper
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App
1. Run the app:
```bash
streamlit run app.py
```
2. Access `http://localhost:8501` in your browser.

## Project Structure
```
wordle-helper/
├── app.py                # Streamlit interface
├── wordle_helper.py      # Word search functions
├── test_wordle_helper.py # Unit tests (pytest)
├── README.md             # This file
├── brazilian_words_no_accent.txt    # Brazilian Portuguese word list
└── english_words_alpha.txt          # English word list
```

### Word Lists
- **English**: Based on the [English Words](https://github.com/dwyl/english-words) repository.
- **Portuguese**: Sourced from [IME-USP](https://www.ime.usp.br/~pf/dicios/).

## Tests

### Running Tests
```bash
# Run all tests
pytest test_wordle_helper.py

# Run with coverage report
pytest --cov=wordle_helper test_wordle_helper.py
```
