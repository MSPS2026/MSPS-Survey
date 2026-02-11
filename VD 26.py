import streamlit as st
import base64

st.title("Annual UMMBGB Survey")

if "step" not in st.session_state: 
    st.session_state.step = 1 # initializes to start page count

# Q1
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

# Q3
elif st.session_state.step == 3:
    classification = st.selectbox(
        "What are birds classified as?",
        ["Mammals", "Birds", "Fish", "Reptiles"]
    )

    if st.button("Next"):
        st.session_state.classification = classification
        st.session_state.step = 4
        st.rerun()

# Q4
elif st.session_state.step == 4:
    food = st.selectbox(
        "What do penguins primarily eat?",
        ["Plants", "Fish", "Insects", "Berries"]
    )

    if st.button("Next"):
        st.session_state.food = food
        st.session_state.step = 5
        st.rerun()

# Q5
elif st.session_state.step == 5:
    climate = st.selectbox(
        "Do all penguins live in warm climates?",
        ["Yes", "No"]
    )

    if st.button("Next"):
        st.session_state.climate = climate
        st.session_state.step = 6
        st.rerun()

# Q6
elif st.session_state.step == 6:
    groupOfPenguins = st.selectbox(
        "What is a group of penguins in water called?",
        ["A colony", "A raft", "A flock", "A pod"]
    )

    if st.button("Next"):
        st.session_state.groupOfPenguins = groupOfPenguins
        st.session_state.step = 7
        st.rerun()

# Q7
elif st.session_state.step == 7:
    largest = st.selectbox(
        "Which penguin species is the largest?",
        ["Emperor Penguin", "King Penguin", "Macaroni Penguin", "Little Blue Penguin"]
    )

    if st.button("Next"):
        st.session_state.largest = largest
        st.session_state.step = 8
        st.rerun()

# Q8
elif st.session_state.step == 8:
    continent = st.selectbox(
        "Which continent has NO native penguins?",
        ["Australia", "Africa", "South America", "North America"]
    )

    if st.button("Next"):
        st.session_state.continent = continent
        st.session_state.step = 9
        st.rerun()

# Q9
elif st.session_state.step == 9:
    warm = st.selectbox(
        "Penguins stay warm mainly because of:",
        ["Thick fur", "Blubber and dense feathers", "Large body size only", "Fast swimming"]
    )

    if st.button("Next"):
        st.session_state.warm = warm
        st.session_state.step = 10
        st.rerun()

# Q10
elif st.session_state.step == 10:
    seawater = st.selectbox(
        "How do penguins drink seawater?",
        ["They don’t", "They filter salt through a gland", "They boil it", "They absorb it through skin"]
    )

    if st.button("Next"):
        st.session_state.seawater = seawater
        st.session_state.step = 11
        st.rerun()

# Q11
elif st.session_state.step == 11:
    flight = st.selectbox(
        "Can penguins fly?",
        ["Yes", "No"]
    )

    if flight == "No":
        cannotFly = st.selectbox(
            "Do you think if you covered it in glue and rolled it around with feathers it will learn how to eventually?",
            ["Yes", "No"]
        )

    if st.button("Next"):
        if flight == "No":
            if cannotFly == "No":
                finalFlightAnswer = cannotFly
            else:
                finalFlightAnswer = "Yes, but only when covered in feathers."
        else:
            finalFlightAnswer = flight

        st.session_state.flight = finalFlightAnswer
        st.session_state.step = 12
        st.rerun()

# Q12
elif st.session_state.step == 12:
    wouldYouWatch = st.selectbox(
        "Would you watch a 1 hour documentary about penguins?",
        ["Yes", "No", "Maybe"]
    )

    if st.button("Next"):
        st.session_state.wouldYouWatch = wouldYouWatch
        st.session_state.step = 13
        st.rerun()

# Q13
elif st.session_state.step == 13:
    wouldPenguinsWatch = st.selectbox(
        "Would a penguin watch a 1 hour documentary about you?",
        ["Yes", "No", "Probably Not"]
    )

    if st.button("Next"):
        st.session_state.wouldPenguinsWatch = wouldPenguinsWatch
        st.session_state.step = 14
        st.rerun()

# Q14
elif st.session_state.step == 14:
    thePenguin = st.text_input(
        "What do you think about the penguin who left its colony to head towards the mountains, in search for the unknown? Write your answer here (min. 1000 words):",
    )

    if st.button("Next"):
        st.session_state.thePenguin = thePenguin
        st.session_state.step = 15
        st.rerun()

# Q15
elif st.session_state.step == 15:
    eat = st.selectbox(
        "Would you eat a penguin?",
        ["Yes", "No"]
    )

    if st.button("Next"):
        st.session_state.eat = eat
        st.session_state.step = 16
        st.rerun()

# Q16
elif st.session_state.step == 16:
    amIAPenguin = st.selectbox(
        "Are you a penguin",
        ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
    )

    if st.button("Next"):
        st.session_state.amIAPenguin = amIAPenguin
        st.session_state.step = 17
        st.rerun()

# Instructions
elif st.session_state.step == 17:
    st.write("For the next question, please make sure to turn your volume up as an audio will be played.")

    if st.button("Next"):
        st.session_state.step = 18
        st.rerun()

# Q17
elif st.session_state.step == 18:

    # Load audio file
    with open("earnedit.mp3", "rb") as f:
        audio_bytes = f.read()

    # Convert to base64
    audio_base64 = base64.b64encode(audio_bytes).decode()

    # Hidden audio player (no progress bar)
    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state for current image
    if "penguin" not in st.session_state:
        st.session_state.curr_img = "penguin1.png"

# Show the current image, centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(st.session_state.curr_img, width=400)

    st.write("Will you be Liam Mananghaya's valentine?")

    if st.button("Yes"):
        st.session_state.curr_img = "penguinhappy.jpg"

    if st.button("No"):
        st.session_state.curr_img = "penguinangry.jpg"
        st.write("Think again.")

    if st.button("Next"):
        st.session_state.valentine = valentine
        st.session_state.step = 19
        st.rerun()

# Final page
elif st.session_state.step == 19:
    st.success("")
    st.write("What is your favorite species of penguins?", st.session_state.favSpecies)
    st.write("Where do you think your favorite species of penguins are commonly located?", st.session_state.location)
    st.write("What are birds classified as?", st.session_state.classification)
    st.write("What do penguins primarily eat?", st.session_state.food)
    st.write("Do all penguins live in warm climates?", st.session_state.climate)







