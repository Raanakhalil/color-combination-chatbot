# Step 1: Import necessary libraries
import streamlit as st

# Predefined color combinations
color_combinations = {
    'red': ['white', 'black', 'yellow', 'blue'],
    'blue': ['white', 'gray', 'yellow', 'orange'],
    'green': ['white', 'brown', 'black', 'pink'],
    'yellow': ['blue', 'purple', 'brown', 'green'],
    'orange': ['blue', 'white', 'black'],
    'purple': ['yellow', 'green', 'blue'],
    'pink': ['green', 'black', 'gray'],
    'white': ['red', 'blue', 'black', 'green'],
    'black': ['red', 'white', 'yellow', 'pink'],
}

# Step 2: Define a function to suggest matching colors
def suggest_color(input_color):
    input_color = input_color.lower()
    
    if input_color in color_combinations:
        matches = color_combinations[input_color]
        return f"With {input_color}, you can wear: {', '.join(matches)}."
    else:
        return "Sorry, I don't have suggestions for that color."

# Step 3: Streamlit App Design
st.title("Color Combination Suggestion App")
st.write("Enter a color and get suggestions for matching colors!")

# Step 4: Create an input field for the user to enter a color
input_color = st.text_input("Enter a color:", "")

# Step 5: Display suggestions
if st.button("Suggest Color"):
    if input_color:
        suggestion = suggest_color(input_color)
        st.success(suggestion)
    else:
        st.error("Please enter a color.")
