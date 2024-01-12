import streamlit as st
import random


def assign_chores(chores, candidates):
    random.shuffle(candidates)
    assignments = dict(zip(chores, candidates))
    return assignments


def main():
    st.title("Chores Assignment App")

    chores = ["GARBAGE + VACUUM", "MOPING THE FLOORS", "CLEANING THE TOILET + WIPING FURNITURE"]
    candidates = ["ALI", "SEN", "ANIKET"]

    if st.button("Assign Chores"):
        assignments = assign_chores(chores, candidates)
        st.success("Chores assigned successfully!")

        st.subheader("Chores for the Week:")
        for chore, person in assignments.items():
            st.write(f"- {chore}: {person}")

if __name__ == "__main__":
    main()


