import streamlit as st
import random

def simulate_megamillions(total_balls, num_drawn, mega_ball_range):
    """
    Simulates a Mega Millions draw with a separate Mega Ball.
    
    Parameters:
    - total_balls (int): Total number of balls in the main draw.
    - num_drawn (int): Number of balls to be drawn in the main draw.
    - mega_ball_range (int): Range of Mega Ball numbers.
    
    Returns:
    - tuple: List of drawn numbers and the Mega Ball number.
    """
    if num_drawn > total_balls:
        raise ValueError("Number of drawn balls cannot exceed total number of balls.")
    
    # Create a list of balls for the main draw
    balls = list(range(1, total_balls + 1))
    
    # Shuffle the balls to simulate randomness
    random.shuffle(balls)
    
    # Draw the specified number of balls and sort them
    drawn_balls = sorted(balls[:num_drawn])
    
    # Draw the Mega Ball
    mega_ball = random.randint(1, mega_ball_range)
    
    return drawn_balls, mega_ball

# Streamlit interface to set parameters
st.title("Mega Millions Simulation")

total_balls = st.number_input("Total number of balls", min_value=1, value=70)
num_drawn = st.number_input("Number of balls to draw", min_value=1, value=5)
mega_ball_range = st.number_input("Range for Mega Ball", min_value=1, value=25)

if st.button("Generate Lottery Numbers"):
    try:
        drawn_balls, mega_ball = simulate_megamillions(total_balls, num_drawn, mega_ball_range)
        st.write("Drawn Balls:", drawn_balls)
        st.write("Mega Ball:", mega_ball)
    except Exception as e:
        st.error(f"An error occurred: {e}")
