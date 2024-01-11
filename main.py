import streamlit as st
from src.langchain_helper import generate_restaurant_name_and_items

# Page Title and User Instructions
st.title("Restaurant Name Generator")
st.sidebar.markdown("""
### Instructions
1. Type in your country in the input box.
2. Enter the number of restaurants you want to generate (limit: 10).
3. Click the "Generate" button.
4. You should see the generated restaurant names and menu items displayed on the web page.

---
""")

# Improved Layout
col1, col2 = st.columns(2)

# Cuisine Selection
with col1:
    cuisine = st.sidebar.text_input("Enter Your Country")

# Quantity of Random Restaurants
with col2:
    quantity = st.sidebar.number_input("Number of Restaurants", min_value=1, max_value=10, value=1)

# Generate Button
if st.sidebar.button("Generate"):
    for _ in range(quantity):
        response = generate_restaurant_name_and_items(cuisine)
        st.header(response['restaurant_name'].strip())
        menu_items = response['menu_items'].strip().split(",")
        st.markdown("**Menu Items**")
        for item in menu_items:
            st.write(f"- {item.strip()}")
        st.write("---")

# Copyright and Email
st.sidebar.markdown("""
---
For inquiries, please contact:
                    
email: ayodeleayodeji250@gmail.com
                    
LinkedIn: https://www.linkedin.com/in/ayo-ayodeji/
""")

st.sidebar.markdown("""
© 2023 Ayodele Ayodeji. All Rights Reserved.
""")
