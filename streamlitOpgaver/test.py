import streamlit as st

# Slider
x = st.slider('x')
st.write(x, 'squared is', x * x)

# Input
st.text_input("Your name", key="name", type="password")
st.session_state.name

# Markdown
st.markdown("# Page 2 🖥️")

# Titel
st.title("Titel angives her")
