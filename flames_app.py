import streamlit as st

page_bg_img = """
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('<center><h1>🅵🅻🅰🅼🅴🆂</h1></center>',unsafe_allow_html=True)

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )




