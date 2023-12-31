import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png")

with col2:
    st.title("Van Hung Si")
    content = """
    Hello, I'm Van Hung Si, a 31-year-old professional with a passion for technology and a knack for
    problem-solving. By day, I lead a dynamic team as a Warehouse Document Team Leader, ensuring seamless operations 
    and meticulous record-keeping.

    In my spare time, I've immersed myself in the world of Python programming, leveraging its power to tackle various 
    challenges and create solutions that streamline processes and enhance efficiency.
    """
    st.info(content)
content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.text(content2)

col3, mt_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
