import streamlit as st
from src.langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name Generator")


# Page Title and User Instructions
st.sidebar.markdown("""
### Instructions
1. Choose a cuisine from the sidebar.
2. Select the number of restaurants you want to generate from the dropdown.
3. Click the "Generate" button.
4. You should see the generated restaurant names and menu items displayed on the web page.
""")


# Improved Layout
col1, col2 = st.columns(2)

# Cuisine Selection
with col1:
    cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Nigeria", "Indian", "Italian", "Mexican", "Arabic", "American"))

# Quantity of Random Restaurants
with col2:
    quantity = st.sidebar.selectbox("Number of Restaurants", range(1, 11), 1)

# Generate Button
if st.sidebar.button("Generate"):
    for _ in range(quantity):
        response = generate_restaurant_name_and_items(cuisine)
        st.subheader(response['restaurant_name'].strip())
        menu_items = response['menu_items'].strip().split(",")
        st.markdown("**Menu Items**")
        for item in menu_items:
            st.write(f"- {item.strip()}")
        st.write("---")


# Copyright and Email
st.sidebar.markdown("""
---
For inquiries, please contact: ayodeleayodeji250@gmail.com
""")

st.sidebar.markdown("""
© 2023 Ayodele Ayodeji. All Rights Reserved.
""")