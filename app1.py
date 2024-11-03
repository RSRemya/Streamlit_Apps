import streamlit as st

#Title
st.title("Streamlit for ML Projects")
st.header("Header")
st.subheader("Subheader")
st.text("hello streamlit")
st.markdown("learn markdown")
st.markdown("# using markdown to create title")
st.markdown("## using markdown to create header")
st.markdown("### using markdown to create subheader")
st.success("sending success message")
st.info("sending information")
st.warning("sending warning")
st.error("sending error message")
st.exception("Name error")
import pandas
st.help(pandas)
st.help(range)
st.write("using write function")
st.write(range(10))
from PIL import Image
img = Image.open("1.jfif")
st.image(img)
