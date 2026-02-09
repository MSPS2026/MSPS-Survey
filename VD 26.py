import streamlit as st

st.title("Annual UMMBGB Survey")

if "step" not in st.session_state: 
    st.session_state.step = 1 # initializes to start page count

if st.session_state.step == 1:
    favSpecies = st.selectbox(
        "What is your favorite species of penguins?",
        ["Emperor Penguin", "King Penguin", "Macaroni Penguin", "Little Penguin", "Other"]
    )

    if favSpecies == "Other":
        otherSpecies = st.text_input("Please specify:")

    if st.button("Next"):
        if favSpecies == "Other":
            finalSpecies = otherSpecies
        else:
            finalSpecies = favSpecies
        
        st.session_state.favSpecies = favSpecies
        st.session_state.step = 2
        st.rerun()

# Q2
elif st.session_state.step == 2:
    location = st.text_input(
        "Where do you think your favorite species of penguins are commonly located?"
    )

    if st.button("Next"):
        st.session_state.location = location
        st.session_state.step = 3
        st.rerun()

# Final page
elif st.session_state.step == 3:
    st.success("Survey Complete! On behalf of the University of Manitoba's Most Beautiful Girl's Boyfriend (UMMBGB), we thanks for expressing an interest in learning about penguins! Here is a summary of your answers:")
    st.write("Species:", st.session_state.species)
    st.write("Location:", st.session_state.location)

