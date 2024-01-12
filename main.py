import streamlit as st
import random

# Chores and Candidates
chores = ["GARBAGE + VACUUM", "MOPING THE FLOORS", "CLEANING THE TOILET + WIPING FURNITURE"]
candidates = ["ALI", "SEN", "ANIKET"]

# Function to randomly assign chores to candidates
def assign_chores():
    random.shuffle(candidates)
    return {chores[i]: candidates[i] for i in range(len(chores))}

# UI
st.title("Weekly Chores Assignment")

# Button to assign candidates
if st.button("Assign Candidates"):
    st.session_state["assigned_chores"] = assign_chores()
    st.success("Chores assigned successfully!")

# Display assigned chores
if 'assigned_chores' in st.session_state:
    st.subheader("This week's assigned chores:")
    for chore, candidate in st.session_state["assigned_chores"].items():
        st.info(f"{chore}: {candidate}")

# Checklist for marking off completed chores
st.subheader("Mark off completed chores:")
completed_chores = st.checkbox("GARBAGE + VACUUM")
if completed_chores:
    st.success("Chore completed!")

completed_chores = st.checkbox("MOPING THE FLOORS")
if completed_chores:
    st.success("Chore completed!")

completed_chores = st.checkbox("CLEANING THE TOILET + WIPING FURNITURE")
if completed_chores:
    st.success("Chore completed!")
