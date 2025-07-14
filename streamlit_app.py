import streamlit as st

st.title("Inner Uplift ✨")

st.markdown("**Fill this out to begin your healing message:**")

x = st.text_input("I remember when...")
y = st.text_input("It made me feel...")
z = st.text_input("Now, because...")
n = st.text_input("I want to hear...")

tone = st.selectbox("Pick a style:", ["Calming", "Funny", "Amped Up", "Hard Hitting", "Out of this world"])

if st.button("Generate Message"):
    st.markdown("#### Your Custom Healing Message:")
    st.write(f"You're not alone. You remember when {x}, and it made you feel {y}. But now, because {z}, you're ready to hear this: {n}. Let it sink in, {tone.lower()} style.")
    st.markdown("*(AI voice coming soon...)*")
