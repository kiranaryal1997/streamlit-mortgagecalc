import streamlit as st

st.set_page_config(page_title="Kiran Aryal")

#markdown formatting by default
st.write("""## Check""")

st.title("Learning Streamlit")

my_name = st.text_input("What is your name?")

st.write("Your name is", my_name)

is_clicked = st.button("Click Me")