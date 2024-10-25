import streamlit as st

def quiz_game():
    st.title("Nyoba bikin Quiz #python")

    score = 0

    # Pertanyaan 1
    st.subheader("What is Angie's favorite food? (wrong answer only)")
    food = st.radio("Choose one", ['Pizza', 'NasPad', 'Durian', 'Kibbeling'])
    if st.button("Submit Answer 1"):
        if food == 'Durian':
            st.success("Yeaaaay bener")
            score += 1
        else:
            st.error("Lho kok salaah!")

    # Pertanyaan 2
    st.subheader("Angie lahir tahun berapa?")
    year = st.radio("Choose one", ['2001', '2002', '2000', '1999'])
    if st.button("Submit Answer 2"):
        if year == '2001':
            st.success("Kereeen inget")
            score += 1
        else:
            st.error("Bete deh")

    # Pertanyaan 3
    st.subheader("Angie sering kelas dmn?")
    place = st.radio("Choose one", ['Orion', 'Lebo', 'Aurora', 'Forum'])
    if st.button("Submit Answer 3"):
        if place == 'Lebo':
            st.success("Bagussss")
            score += 1
        else:
            st.error("MASA LUPA?!")

    # Pertanyaan 4
    st.subheader("Apa gambar di gantungan tas angie?")
    animal = st.radio("Choose one", ['Paus', 'Pinguin', 'Kucing', 'Anjing'])
    if st.button("Submit Answer 4"):
        if animal == 'Pinguin':
            st.success("Hahahah nice")
            score += 1
        else:
            st.error("Parah bgt")

    # Pertanyaan 5
    st.subheader("Apa warna hoodie WUR angie?")
    color = st.radio("Choose one", ['Ijo', 'Biru', 'Maroon', 'Putih'])
    if st.button("Submit Answer 5"):
        if color == 'Ijo':
            st.success("Fiuh kirain km lupaa")
            score += 1
        else:
            st.error("Teganyaaaaa")


if __name__ == "__main__":
    quiz_game()
