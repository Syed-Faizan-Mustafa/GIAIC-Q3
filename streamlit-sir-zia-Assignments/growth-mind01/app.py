import streamlit as st

st.title("🌱 Growth Mindset App")

st.write("Welcome to the Growth Mindset App! Here you can set goals, track progress, and stay motivated.")

# Goal Setting
goal = st.text_input("Set your goal:")
if st.button("Save Goal"):
    st.success(f"Goal Saved: {goal}")

# Progress Tracker
progress = st.slider("Track your progress:", 0, 100, 0)
st.progress(progress / 100)

# Daily Inspiration
st.subheader("🌟 Daily Inspiration")
st.write("Keep pushing forward! Every step counts.")