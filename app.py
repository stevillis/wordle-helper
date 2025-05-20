import streamlit as st

from wordle_helper import find_words, get_five_letter_words

if __name__ == "__main__":
    st.set_page_config(page_title="Wordle Helper", layout="wide")
    st.title("Wordle Helper")

    st.sidebar.selectbox(
        "Language",
        options=["english", "português"],
        index=1,
        key="language",
    )

    language = st.session_state.language

    if language == "english":
        st.markdown(
            """
            This app helps you to find 5 letter words to the game [Wordle](https://wordle.com/).

            - Type the known letters in the correct positions. Leave blank
            the positions you don't know.
            - Click on **Search** to see the candidate words.

            **Example:** If you know that the second letter is 'A', fill
            only the second box.
        """,
            unsafe_allow_html=True,
        )
    elif language == "português":
        st.markdown(
            """
            Este aplicativo auxilia você a encontrar palavras de 5 letras para o
            jogo [Termo](https://termo.pt/) (Wordle em Português).

            - Digite as letras conhecidas nas posições corretas. Deixe em branco
            as posições desconhecidas.
            - Clique em **Buscar** para ver as palavras candidatas.

            **Exemplo:** Se você sabe que a segunda letra é 'A', preencha
            apenas a segunda caixa.
        """,
            unsafe_allow_html=True,
        )

    candidate_words = []

    if "br_five_letter_words" not in st.session_state:
        st.session_state.br_five_letter_words = get_five_letter_words(
            language="português"
        )

    if "en_five_letter_words" not in st.session_state:
        st.session_state.en_five_letter_words = get_five_letter_words(
            language="english"
        )

    if language == "english":
        SUBHEADER_BODY = "Type the known letters:"
    elif language == "português":
        SUBHEADER_BODY = "Digite as letras conhecidas:"

    st.subheader(SUBHEADER_BODY)

    word_pattern = []
    letter_label = "Letter" if language == "english" else "Letra"
    search_label = "Search" if language == "english" else "Buscar"

    cols = st.columns(5)
    for i, col in enumerate(cols):
        letter = col.text_input(
            f"{letter_label} {i+1}", key=f"letter_{i+1}", max_chars=1
        )
        word_pattern.append(letter.lower() if letter else "")

    if st.button(search_label, use_container_width=True):
        if language == "english":
            candidate_words = find_words(
                st.session_state.en_five_letter_words, word_pattern
            )
        else:
            candidate_words = find_words(
                st.session_state.br_five_letter_words, word_pattern
            )

        if not any(word_pattern):
            error_message = (
                "Fill at least one letter."
                if language == "english"
                else "Preencha pelo menos uma letra."
            )
            st.error(error_message)
        else:
            if candidate_words:
                success_message = (
                    f"{len(candidate_words)} word(s) found:"
                    if language == "english"
                    else f"{len(candidate_words)} palavra(s) encontrada(s):"
                )
                st.success(success_message)
                st.write(
                    f"""
                    <div style="max-height: 250px; overflow-y: auto;">
                        {"<br>".join(candidate_words)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif any(word_pattern):
                warning_message = (
                    "No words found for the given pattern."
                    if language == "english"
                    else "Nenhuma palavra encontrada para o padrão informado."
                )
                st.warning(warning_message)
