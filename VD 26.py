import streamlit as st

st.title("Annual MBAGM Survey")

favSpecies = st.selectbox(
    "What is your favorite species of penguins?",
    ["Emperor Penguin", "King Penguin", "Macaroni Penguin", "Little Penguin", "Other"]
)

if favSpecies == "Other":
    otherSpecies = st.text_input("Please specify:")

if st.button("Submit"):
    if favSpecies == "Other":
        finalSpecies = otherSpecies
    else:
        finalSpecies = favSpecies

birds = st.selectbox(
    "Are penguins birds?",
    ["Yes", "No", "Not sure"]
)
