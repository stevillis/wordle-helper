import streamlit as st

from wordle_helper import find_words, get_five_letter_words

if __name__ == "__main__":
    st.title("Wordle Helper")
    st.markdown(
        """
        Este aplicativo auxilia você a encontrar palavras de 5 letras para
        jogos como o [Wordle](https://www.nytimes.com/games/wordle/index.html).

        - Digite as letras conhecidas nas posições corretas. Deixe em branco
        as posições desconhecidas.
        - Clique em **Buscar** para ver as palavras candidatas.

        **Exemplo:** Se você sabe que a segunda letra é 'A', preencha
        apenas a segunda caixa.
        """,
        unsafe_allow_html=True,
    )

    candidate_words = []

    if "five_letter_words" not in st.session_state:
        st.session_state.five_letter_words = get_five_letter_words()

    st.subheader("Digite as letras conhecidas:")
    cols = st.columns(5)
    word_pattern = []
    for i, col in enumerate(cols):
        letter = col.text_input(f"Letra {i+1}", key=f"letter_{i+1}", max_chars=1)
        word_pattern.append(letter.lower() if letter else "")

    if st.button("Buscar", use_container_width=True):
        candidate_words = find_words(st.session_state.five_letter_words, word_pattern)

        if not any(word_pattern):
            st.error("Preencha pelo menos uma letra.")
        else:
            if candidate_words:
                st.success(f"{len(candidate_words)} palavra(s) encontrada(s):")
                st.write(
                    f"""
                    <div style="max-height: 250px; overflow-y: auto;">
                        {"<br>".join(candidate_words)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            elif any(word_pattern):
                st.warning("Nenhuma palavra encontrada para o padrão informado.")
