import streamlit as st
import random
from datetime import datetime, timedelta

chores = ["GARBAGE + VACUUM", "MOPING THE FLOORS", "CLEANING THE TOILET + WIPING FURNITURE"]
candidates = ["ALI", "SEN", "ANIKET"]


@st.cache_data(persist="disk")
def assign_chores():
    random.shuffle(candidates)
    return datetime.now(), {chores[i]: candidates[i] for i in range(len(chores))}


def is_week_passed(last_assigned_time):
    current_time = datetime.now()
    time_difference = current_time - last_assigned_time
    return time_difference >= timedelta(days=7)


last_assigned_timestamp, assigned_chores = assign_chores()

if is_week_passed(last_assigned_timestamp):
    assign_chores.clear()
    last_assigned_timestamp, assigned_chores = assign_chores()

st.title("Weekly Chores Assignment")

if assigned_chores:
    st.subheader("This week's assigned chores:")
    for chore, candidate in assigned_chores.items():
        st.info(f"{chore}: {candidate}")

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
